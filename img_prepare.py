import rasterio
import numpy as np
import matplotlib.pyplot as plt

class imgPrepare:

    def __init__(self, file_path, ndvi_min=-1, ndvi_max=1):
        self.ndvi_min = ndvi_min
        self.ndvi_max = ndvi_max
        self.file_path = file_path

    def prepare(self):
        with rasterio.open(f"{self.file_path}") as src:
            org_img = src.read()

        img_plot = np.array(org_img[4])

        ndvi_data = ((((self.ndvi_max - self.ndvi_min) / 255) * org_img) - 1)

        forest_data = np.zeros((org_img.shape[1], org_img.shape[2]), dtype=np.int8)

        for i in range(org_img.shape[1]):
            for j in range(org_img.shape[2]):
                if img_plot[i, j] >= 0.7:
                    forest_data[i, j] = 1

        plt.imshow(forest_data, cmap='hot', interpolation='nearest')
        plt.show()

        ndvi_resume = {"min": ndvi_data.min(),
                       "max": ndvi_data.max(),
                       "mean": ndvi_data.mean()}

        hist_data = ndvi_data.flatten()

        return ndvi_resume, hist_data, ndvi_data
