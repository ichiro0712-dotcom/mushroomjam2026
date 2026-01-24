from PIL import Image, ImageChops
import os

# Source paths (from artifacts/brain)
BRAIN_DIR = "/Users/kawashimaichirou/.gemini/antigravity/brain/688c514c-6e8c-4bdc-ac91-39cef0281565"
DEST_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"

# Map source filename part to destination filename
# Added kikurage
image_map = {
    "shimeji_mushroom": "shimeji_new.png",
    "enoki_mushroom": "enoki_new.png",
    "shiitake_mushroom": "shiitake_new.png",
    "kikurage_mushroom": "kikurage_new.png",
    "eringi_mushroom": "eringi_new.png",
    "matsutake_mushroom": "matsutake_new.png",
    "uploaded_image": "logo_new.png"
}

def process_image(img):
    img = img.convert("RGBA")
    
    # 1. Flood fill from corners to detect background
    # We add a white border first to ensure flood fill can reach around the image
    temp_img = Image.new("RGBA", (img.width + 2, img.height + 2), (255, 255, 255, 255))
    temp_img.paste(img, (1, 1))
    
    # Seed points for flood fill (corners)
    seeds = [(0, 0), (temp_img.width - 1, 0), (0, temp_img.height - 1), (temp_img.width - 1, temp_img.height - 1)]
    
    # Create a mask for flood fill
    # 0 = background, 1 = foreground
    # Image.floodfill isn't directly available in PIL like paint bucket, but we can do a diff based approach
    # Or simplified: Iterate pixels? No, too slow.
    # PIL doesn't have a native "flood fill to transparent".
    # Implementation: Use a simple BFS for flood fill on pixel access (for small images this is fine)
    # Actually, simpler: Use distinct color for background.
    
    # Let's write a manual BFS flood fill
    width, height = temp_img.size
    pixels = temp_img.load()
    queue = seeds
    visited = set(seeds)
    
    # Threshold for white background
    threshold = 200
    
    while queue:
        x, y = queue.pop(0)
        r, g, b, a = pixels[x, y]
        
        # If it's effectively white, make it transparent
        if r > threshold and g > threshold and b > threshold:
            pixels[x, y] = (0, 0, 0, 0)
            
            # Add neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # 2. Crop to content
    # Get bounding box of non-zero alpha
    bbox = temp_img.getbbox()
    if bbox:
        temp_img = temp_img.crop(bbox)
        
    return temp_img

# Find actual files in brain dir
found_files = {}
for f in os.listdir(BRAIN_DIR):
    for key in image_map.keys():
        if key in f and f.endswith(".png"):
            # Check timestamps to get latest? Just overwrite is fine.
            # But wait, generated images have timestamps.
            # We should pick the *most recent* match for each key to ensure we don't pick old failed gens.
            current_path = os.path.join(BRAIN_DIR, f)
            if key not in found_files:
                found_files[key] = current_path
            else:
                # Compare modified times
                if os.path.getmtime(current_path) > os.path.getmtime(found_files[key]):
                    found_files[key] = current_path

# Process and save
for key, src_path in found_files.items():
    dest_filename = image_map[key]
    dest_path = os.path.join(DEST_DIR, dest_filename)
    
    try:
        print(f"Processing {src_path} -> {dest_path}")
        img = Image.open(src_path)
        img = process_image(img)
        img.save(dest_path, "PNG")
        print(f"Saved {dest_filename}")
    except Exception as e:
        print(f"Error processing {key}: {e}")

print("Done processing images.")
