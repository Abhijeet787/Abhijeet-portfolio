import os
import struct
import json

def get_image_size(fname):
    try:
        with open(fname, 'rb') as fhandle:
            head = fhandle.read(24)
            if head[0:4] == b'\x89PNG':
                w, h = struct.unpack('>ii', head[16:24])
                return int(w), int(h)
            elif head[0:2] == b'\xff\xd8':
                fhandle.seek(0)
                fhandle.read(2)
                b = fhandle.read(1)
                while (b and b != b'\xda'):
                    while (b != b'\xff'): b = fhandle.read(1)
                    while (b == b'\xff'): b = fhandle.read(1)
                    if (b >= b'\xc0' and b <= b'\xc3'):
                        fhandle.read(3)
                        h, w = struct.unpack('>HH', fhandle.read(4))
                        return int(w), int(h)
                    else:
                        fhandle.read(int(struct.unpack('>H', fhandle.read(2))[0])-2)
                    b = fhandle.read(1)
    except Exception:
        pass
    return None

results = {}
root_dir = "/Users/abhijeetsinghrathore/Documents/abhijeet portfolio/project_creatives"
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            full_path = os.path.join(root, f)
            size = get_image_size(full_path)
            if size:
                rel_path = os.path.relpath(full_path, "/Users/abhijeetsinghrathore/Documents/abhijeet portfolio")
                parts = rel_path.split(os.sep)
                # parts[0] is 'project_creatives', parts[1] is the project id
                project_id = parts[1]
                if project_id not in results:
                    results[project_id] = []
                results[project_id].append({
                    "file": f,
                    "width": size[0],
                    "height": size[1],
                    "ratio": round(size[0] / size[1], 4)
                })

for proj, imgs in results.items():
    print(f"Project: {proj}")
    for img in imgs:
        print(f"  {img['file']}: {img['width']}x{img['height']} (Ratio: {img['ratio']})")
