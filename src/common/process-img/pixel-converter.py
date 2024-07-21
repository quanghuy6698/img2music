import cv2
import numpy as np

img_file_path = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3.png"

image = cv2.imread(img_file_path)
img_h, img_w = image.shape[:2]
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_array = np.array(image_rgb)

out_file_path = "E:/thac-si-cntt-TLU/final-project/img2music/asset/demo/leaves3.txt"
f = open(out_file_path, "a")
for i in pixel_array:
    for j in i:
        f.write(str(j))
        f.write('\n')
f.close()
