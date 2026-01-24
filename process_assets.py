from PIL import Image
import os
import shutil

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

def remove_white_bg(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        # Change all white (also shades of whites) to transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
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
        print(f"Processing {src_path} -> {dest_path}")
        img = Image.open(src_path)
        img = remove_white_bg(img)
        img.save(dest_path, "PNG")
        print(f"Saved {dest_filename}")
    except Exception as e:
        print(f"Error processing {key}: {e}")

print("Done processing images.")
