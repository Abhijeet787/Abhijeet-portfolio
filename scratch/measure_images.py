import os
import struct
import json

def get_image_size(fname):
    try:
        with open(fname, 'rb') as fhandle:
            head = fhandle.read(24)
            if len(head) != 24:
                return None
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
                return None
            else:
                return None
    except Exception as e:
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
                results[rel_path] = size

print(json.dumps(results, indent=2))
