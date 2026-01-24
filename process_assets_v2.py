from PIL import Image, ImageFilter
import os

# Source paths (from artifacts/brain)
BRAIN_DIR = "/Users/kawashimaichirou/.gemini/antigravity/brain/688c514c-6e8c-4bdc-ac91-39cef0281565"
DEST_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"

# Map source filename part to destination filename
image_map = {
    "shimeji_mushroom": "shimeji_new.png",
    "enoki_mushroom": "enoki_new.png",
    "shiitake_mushroom": "shiitake_new.png",
    "eringi_mushroom": "eringi_new.png",
    "matsutake_mushroom": "matsutake_new.png",
    "uploaded_image": "logo_new.png"
}

def clean_transparency(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    
    # Threshold for what is considered "white background"
    # Since the prompt asked for "isolated on white background", we can be aggressive.
    bg_threshold = 200
    
    for item in datas:
        # Check if pixel is close to white
        if item[0] > bg_threshold and item[1] > bg_threshold and item[2] > bg_threshold:
            new_data.append((255, 255, 255, 0)) # Fully transparent
        else:
            new_data.append(item)
    
    img.putdata(new_data)
    
    # Remove white fringe/halo caused by anti-aliasing against white background
    # Create a mask of non-transparent pixels
    r, g, b, a = img.split()
    
    # Erode the alpha channel slightly to eat into the white fringe
    # This is a simple trick: perform min filter on alpha
    # But standard min filter might be too strong (removes 1px hard). 
    # Let's try iterating through pixels to remove whitish semi-transparent ones.
    
    cleaned_data = []
    datas = img.getdata()
    for item in datas:
        r, g, b, a = item
        # If the pixel is semi-transparent and very light (white fringe), kill it
        if a > 0 and a < 255 and r > 150 and g > 150 and b > 150:
             cleaned_data.append((r, g, b, 0))
        else:
             cleaned_data.append(item)
    
    img.putdata(cleaned_data)
    return img

# Find actual files in brain dir
found_files = {}
for f in os.listdir(BRAIN_DIR):
    for key in image_map.keys():
        if key in f and f.endswith(".png"):
            found_files[key] = os.path.join(BRAIN_DIR, f)

# Process and save
for key, src_path in found_files.items():
    dest_filename = image_map[key]
    dest_path = os.path.join(DEST_DIR, dest_filename)
    
    try:
        print(f"Reprocessing {src_path} -> {dest_path}")
        img = Image.open(src_path)
        img = clean_transparency(img)
        img.save(dest_path, "PNG")
        print(f"Saved {dest_filename}")
    except Exception as e:
        print(f"Error processing {key}: {e}")

print("Done reprocessing images.")
