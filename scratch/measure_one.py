import struct

def get_image_size(fname):
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
    return None

print("holipurim:", get_image_size("project_creatives/holipurim-2026/holipurim creatives/Holipurimcreative.jpg"))
