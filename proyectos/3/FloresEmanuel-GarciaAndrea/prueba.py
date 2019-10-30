import mmap

with open("fiunamfs.img", 'r+b') as f:
    file_map = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    print(file_map[2048:2048+64])