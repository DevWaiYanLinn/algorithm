import os
import glob
import numpy as np
import shutil

# os.chmod("./src", 0o755)
image_files = []
for root, dirs, files in os.walk('./all-data'):
    if len(files):
        arr = np.array(files)
        np.random.shuffle(arr)
        dst = root.replace('./all-data\\', '')
        os.makedirs(os.path.join("src", dst), exist_ok=True)
        for file in arr[0:3000]:
            path = os.path.join(root, file)
            shutil.copy2(path, os.path.join("src", dst))
