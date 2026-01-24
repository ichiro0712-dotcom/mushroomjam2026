from PIL import Image, ImageChops, ImageOps
import os

# Source paths (from artifacts/brain)
BRAIN_DIR = "/Users/kawashimaichirou/.gemini/antigravity/brain/688c514c-6e8c-4bdc-ac91-39cef0281565"
DEST_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"

# Map source filename part to destination filename
image_map = {
    # Using v2 for new generations
    "shiitake_mushroom_v2": "shiitake_new.png",
    "matsutake_mushroom_v2": "matsutake_new.png",
    # Keep others same
    "shimeji_mushroom": "shimeji_new.png",
    "enoki_mushroom": "enoki_new.png",
    "kikurage_mushroom": "kikurage_new.png",
    "eringi_mushroom": "eringi_new.png",
    "uploaded_image": "logo_new.png"
}

def invert_colors(img):
    # Invert colors (black -> white)
    # Handle alpha channel: only invert RGB, keep Alpha
    if img.mode == 'RGBA':
        r, g, b, a = img.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        inverted_image = ImageOps.invert(rgb_image)
        r2, g2, b2 = inverted_image.split()
        return Image.merge('RGBA', (r2, g2, b2, a))
    else:
        return ImageOps.invert(img)

def process_image(img, is_logo=False):
    img = img.convert("RGBA")
    
    # 1. Flood fill from corners to detect background
    temp_img = Image.new("RGBA", (img.width + 2, img.height + 2), (255, 255, 255, 255))
    temp_img.paste(img, (1, 1))
    
    seeds = [(0, 0), (temp_img.width - 1, 0), (0, temp_img.height - 1), (temp_img.width - 1, temp_img.height - 1)]
    
    width, height = temp_img.size
    pixels = temp_img.load()
    queue = seeds
    visited = set(seeds)
    
    # Threshold for white background (flood fill)
    threshold = 200
    
    if is_logo:
        # For logo, if we invert it first, the background (white) becomes black.
        # So we should process transparency FIRST, then invert?
        # OR invert first?
        # Original: Black logo on white background.
        # Step 1: Make white background transparent.
        # Step 2: Invert Black logo to White logo.
        pass
    
    # Standard flood fill to remove white background
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
        
    if is_logo:
        # Invert colors after making background transparent
        # Non-transparent pixels (black logo) should become white
        temp_img = invert_colors(temp_img)
        
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
    
    is_logo = (key == "uploaded_image")
    
    try:
        print(f"Processing {src_path} -> {dest_path} (Logo: {is_logo})")
        img = Image.open(src_path)
        img = process_image(img, is_logo=is_logo)
        img.save(dest_path, "PNG")
        print(f"Saved {dest_filename}")
    except Exception as e:
        print(f"Error processing {key}: {e}")

print("Done processing images (v4).")
