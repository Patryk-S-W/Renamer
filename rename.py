# Rename all JPG and PNG images in the current directory
# to p0.jpg, p1.jpg, p2.png etc.

import os

i = 0
for filename in os.listdir("."):
    os.rename(filename, filename.lower())
    if filename.endswith(".png"):
        os.rename(filename, "p"+str(i)+".png")
        i = i + 1
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        os.rename(filename, "p"+str(i)+".jpg")
        i = i + 1
