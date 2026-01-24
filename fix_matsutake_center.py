from PIL import Image, ImageDraw
import os

# Paths
IMG_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"
MATSUTAKE_PATH = os.path.join(IMG_DIR, "matsutake_new.png")

def fill_center_black():
    try:
        img = Image.open(MATSUTAKE_PATH).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        # Center point
        cx, cy = width // 2, height // 2
        
        # Check if center is white-ish (meaning it wasn't cleared by corner flood fill)
        # or transparent (if the generation made it transparent, but user wants black)
        r, g, b, a = pixels[cx, cy]
        
        # Flood fill target: Black (0,0,0,255)
        # Determine start condition
        target_color = (r, g, b, a)
        
        print(f"Center pixel color at ({cx}, {cy}): {target_color}")
        
        # Perform flood fill from center
        # We want to change the 'hole' to black.
        # If the hole is white (255, 255, 255, 255) -> Change to Black
        # If the hole is transparent (0, 0, 0, 0) -> Change to Black
        
        # Using ImageDraw.floodfill (available in recent Pillow)
        # Tolerence might be needed if it's not pure white
        
        ImageDraw.floodfill(img, (cx, cy), (0, 0, 0, 255), thresh=50)
        
        img.save(MATSUTAKE_PATH)
        print(f"Successfully filled center of {MATSUTAKE_PATH} with black.")
        
    except Exception as e:
        print(f"Error processing matsutake: {e}")

if __name__ == "__main__":
    fill_center_black()
