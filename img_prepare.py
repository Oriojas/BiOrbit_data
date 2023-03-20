import rasterio
import numpy as np
import matplotlib.pyplot as plt


class imgPrepare:

    def __init__(self, file_path, ndvi_min=-1, ndvi_max=1):
        self.ndvi_min = ndvi_min
        self.ndvi_max = ndvi_max
        self.file_path = file_path

    @property
    def prepare(self):
        with rasterio.open(f"{self.file_path}") as src:
            org_img = src.read()

        deforestation = np.array(org_img[4])

        # ndvi_data = ((((self.ndvi_max - self.ndvi_min) / 255) * org_img) - 1)

        forest_data = np.zeros((org_img.shape[1], org_img.shape[2]), dtype=np.int8)

        for i in range(org_img.shape[1]):
            for j in range(org_img.shape[2]):
                if np.isnan(deforestation[i, j]):
                    deforestation[i, j] = 0
                elif deforestation[i, j] > 1:
                    deforestation[i, j] = 1
                elif deforestation[i, j] >= 0.7:
                    forest_data[i, j] = 1

        # plt.imshow(forest_data, cmap='hot', interpolation='nearest')
        # plt.show()
        area_pixels = deforestation.shape[0] * deforestation.shape[1]
        area_forest = forest_data.sum()

        resume = {"mean": deforestation.mean(),
                  "total_px": area_pixels,
                  "deforestation": area_pixels - area_forest,
                  "percentage": round((1 - (area_forest / area_pixels)) * 100, 2)}

        hist_data = deforestation.flatten()

        return resume, hist_data, deforestation
