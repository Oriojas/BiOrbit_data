import os
import base64
import numpy as np
import download_sat_img as dsi
import matplotlib.pyplot as plt
import matplotlib.image as img

TOKEN = os.getenv("TOKEN")

box = [13.822174072265625, 45.85080395917834,
       14.55963134765625, 46.29191774991382]

raw_img = dsi.downloadSatImg(coord=box, token=TOKEN).img()

sat_img = base64.decodebytes(b"{response.text}")

sat_img = np.asarray(sat_img)

plt.imshow(sat_img)

print(raw_img)
