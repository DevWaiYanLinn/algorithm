import os
import glob

image_files = [];
for root,dirs,files in os.walk('./hello'):
    print(root,files)
    # image_files.extend(glob.glob(os.path.join(root,'*.txt')))

# print(image_files)