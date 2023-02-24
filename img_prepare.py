import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

FILE = "img_input/2020-03-18-00_00_2020-03-18-23_59_Sentinel-2_L2A_True_color.png"

coords = {"type": "Polygon",
          "coordinates": [[[-68.932746, 2.114557],
                           [-70.305524, 2.114557],
                           [-70.305524, 3.622349],
                           [-68.932746, 3.622349],
                           [-68.932746, 2.114557]]]}

org_img = Image.open(FILE)
raw_img = org_img.convert('L')
array_img = np.asarray(raw_img.getdata(), dtype=np.float64).reshape((raw_img.size[1],
                                                                     raw_img.size[0]))

array_img = np.asarray(array_img, dtype=np.int16)
img = Image.fromarray(array_img)

plt.imshow(np.asarray(org_img))
plt.show()
