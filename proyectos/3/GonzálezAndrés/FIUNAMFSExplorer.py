import os
from fiunamfs import FIUNAMFS

fsimg_path = os.path.join('..', 'fiunamfs.img')

fs = FIUNAMFS(fsimg_path)
fs.mount()
fs.umount()