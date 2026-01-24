from PIL import Image, ImageDraw
import os

# Paths
IMG_DIR = "/Users/kawashimaichirou/Desktop/バイブコーディング/mushroomstamps/img"
MATSUTAKE_PATH = os.path.join(IMG_DIR, "matsutake_new.png")

def fix_matsutake_hole():
    try:
        img = Image.open(MATSUTAKE_PATH).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        # We are looking for a hole. 
        # Scan the horizontal center line.
        # We expect: Transparent (outside) -> Colored (Body) -> Transparent/White (Hole) -> Colored (Body)
        
        y = height // 2
        
        # Find start of body from left
        start_x = 0
        while start_x < width and pixels[start_x, y][3] == 0:
            start_x += 1
            
        print(f"Body starts at {start_x}")
        
        # Find end of body (start of hole?)
        # Search for transparency or white AFTER the body starts
        hole_x = start_x
        while hole_x < width:
            r, g, b, a = pixels[hole_x, y]
            is_transparent = (a == 0)
            is_white = (r > 240 and g > 240 and b > 240)
            
            # If we hit transparent/white, checks if we hit the hole or the outside
            if is_transparent or is_white:
                # Check if there is more body to the right (ensures it's a hole)
                remaining_pixels = [pixels[kx, y][3] for kx in range(hole_x + 1, width)]
                if any(alpha > 0 for alpha in remaining_pixels):
                     # Found the hole!
                     print(f"Found hole candidate at {hole_x}, {y}. Color: {pixels[hole_x, y]}")
                     ImageDraw.floodfill(img, (hole_x, y), (0, 0, 0, 255), thresh=50)
                     img.save(MATSUTAKE_PATH)
                     print("Filled hole with black.")
                     return
            hole_x += 1
            
        print("Could not find a hole along the center line.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fix_matsutake_hole()
