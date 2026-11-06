import os
import shutil

src_dir = "/Users/abhijeetsinghrathore/Documents/abhijeet portfolio"
dest_dir = os.path.join(src_dir, "dist")

print("Starting build of clean dist directory inside workspace...")

if os.path.exists(dest_dir):
    print(f"Removing existing dist directory...")
    shutil.rmtree(dest_dir)

os.makedirs(dest_dir)
print(f"Created clean dist directory")

items_to_copy = [
    "index.html",
    "favicon.png",
    "apple-touch-icon.png",
    "bg.jpg",
    "color bg2.jpg",
    "ALARM OF DOME BYOB.jpg",
    "bottom_deck_icons",
    "Floating project icons jpg",
    "project_creatives",
    "my photographs"
]

for item in items_to_copy:
    src_path = os.path.join(src_dir, item)
    dest_path = os.path.join(dest_dir, item)
    
    if not os.path.exists(src_path):
        print(f"WARNING: {item} does not exist!")
        continue
        
    if os.path.isdir(src_path):
        print(f"Copying folder {item}...")
        shutil.copytree(src_path, dest_path)
    else:
        print(f"Copying file {item}...")
        shutil.copy2(src_path, dest_path)

# Calculate size
total_size = 0
for root, dirs, files in os.walk(dest_dir):
    for f in files:
        fp = os.path.join(root, f)
        total_size += os.path.getsize(fp)

size_mb = total_size / (1024 * 1024)
print(f"\nDist directory built successfully!")
print(f"Location: {dest_dir}")
print(f"Total Size: {size_mb:.2f} MB")
