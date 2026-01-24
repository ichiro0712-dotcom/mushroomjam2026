from PIL import Image, ImageChops, ImageOps
import os

# Source paths (from artifacts/brain)
BRAIN_DIR = "/Users/kawashimaichirou/.gemini/antigravity/brain/688c514c-6e8c-4bdc-ac91-39cef0281565"
DEST_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"

# Map source filename part to destination filename
image_map = {
    # New rounds
    "shimeji_round": "shimeji_new.png",
    "enoki_round": "enoki_new.png",
    "shiitake_round": "shiitake_new.png",
    "kikurage_round": "kikurage_new.png",
    "eringi_round": "eringi_new.png",
    "matsutake_round": "matsutake_new.png",
    # Keep logo processing (finding latest uploaded_image if any, or just not updating if not new)
    # Actually, user said keep the logo but make it center background.
    # We already processed the logo in v4. We don't need to re-process it unless I see a new one.
    # I'll just focus on the mushrooms.
}

def process_image(img):
    img = img.convert("RGBA")
    
    # 1. Flood fill from corners to detect white background
    temp_img = Image.new("RGBA", (img.width + 2, img.height + 2), (255, 255, 255, 255))
    temp_img.paste(img, (1, 1))
    
    seeds = [(0, 0), (temp_img.width - 1, 0), (0, temp_img.height - 1), (temp_img.width - 1, temp_img.height - 1)]
    
    width, height = temp_img.size
    pixels = temp_img.load()
    queue = seeds
    visited = set(seeds)
    
    # Threshold for white background (flood fill)
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

    # Crop
    bbox = temp_img.getbbox()
    if bbox:
        temp_img = temp_img.crop(bbox)
        
    return temp_img

# Find actual files in brain dir
found_files = {}
for f in os.listdir(BRAIN_DIR):
    for key in image_map.keys():
        if key in f and f.endswith(".png"):
             # Get latest
            current_path = os.path.join(BRAIN_DIR, f)
            if key not in found_files:
                found_files[key] = current_path
            else:
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

print("Done processing rounding images (v5).")
