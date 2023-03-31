import numpy as np
import img_prepare as ipre
import matplotlib.pyplot as plt

# coords = {"type": "Polygon",
#           "coordinates": [[[-68.932746, 2.114557],
#                            [-70.305524, 2.114557],
#                            [-70.305524, 3.622349],
#                            [-68.932746, 3.622349],
#                            [-68.932746, 2.114557]]]}

FILE = "/img_input/2023-03-14-LC09_B2_B3_B4_B5_multiband_NDVI_masked_added.TIF"

resume, hist, data = ipre.ImgPrepare(file_path=FILE).prepare()

print(resume)

np.savez_compressed("img_output/img", a=data)

plt.boxplot(hist)
plt.show()

loaded = np.load('img_output/img.npz')

print(loaded.f.a.shape)
