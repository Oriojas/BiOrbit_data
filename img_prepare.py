import numpy as np
from PIL import Image


class imgPrepare:

    def __init__(self, file_path, ndvi_min=-1, ndvi_max=1):
        self.ndvi_min = ndvi_min
        self.ndvi_max = ndvi_max
        self.file_path = file_path

    def prepare(self):
        org_img = Image.open(self.file_path)
        raw_img = org_img.convert('L')
        array_img = np.asarray(raw_img.getdata(), dtype=np.float64).reshape((raw_img.size[1],
                                                                             raw_img.size[0]))

        array_img = np.asarray(array_img, dtype=np.int16)
        img = Image.fromarray(array_img)

        ndvi_data = ((((self.ndvi_max - self.ndvi_min) / 255) * array_img) - 1)

        ndvi_resume = {"min": ndvi_data.min(),
                       "max": ndvi_data.max(),
                       "mean": ndvi_data.mean()}

        hist_data = ndvi_data.flatten()

        return ndvi_resume, hist_data, ndvi_data
