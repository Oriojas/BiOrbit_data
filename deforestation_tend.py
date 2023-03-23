import cv2
import json
import numpy as np
import pandas as pd
import img_prepare as ipre
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

with open('/home/oscar/GitHub/BiOrbit_data/img_data/data.json', 'r') as f:
    data = json.load(f)

dict_df = {"date": data["detection_date_list"],
           "deforestation": data["total_extension_forest_cover_list"]}

df = pd.DataFrame.from_dict(dict_df)

df["date"] = df["date"].apply(lambda x: x[0:10])

df["date"] = pd.to_datetime(df["date"])

X_train = np.array(df["date"].apply(lambda x: pd.to_datetime(x).timestamp()))
X_train = X_train.reshape(-1, 1)

y_train = np.array(df["deforestation"])

regr = linear_model.LinearRegression()

regr.fit(X_train, y_train)

y_pred = regr.predict(X_train)

df["pred"] = y_pred

dict_pre = {"date": pd.to_datetime("2023-05-30"),
            "deforestation": regr.predict(np.array(pd.to_datetime("2023-05-30").timestamp()).reshape(-1, 1)),
            "pred": regr.predict(np.array(pd.to_datetime("2023-05-30").timestamp()).reshape(-1, 1))}

df_pred = pd.DataFrame.from_dict(dict_pre)

df = pd.concat([df, df_pred])

# plt.plot(df["date"].iloc[0:-1], df["deforestation"].iloc[0:-1], "-o", label="deforestation")
# plt.plot(df["date"], df["pred"], "--", label="projection")
# plt.hlines(y=data["total_extension_protected_area"],
#            xmin=df["date"].min(), xmax=df["date"].max(),
#            label="total_area", color="green")
#
# plt.title(f"Deforestation: {data['protected_area_name']}, R2={round(r2_score(df['deforestation'], df['pred']), 2)}")
# plt.legend(loc='lower right')
# # plt.yscale("log")
# plt.grid()
# plt.show()

FILE = "/home/oscar/GitHub/BiOrbit_data/img_input/2023-03-14-LC09_B2_B3_B4_B5_multiband_NDVI_masked_added.TIF"

ipre_obj = ipre.ImgPrepare(file_path=FILE)

_, _, data = ipre_obj.prepare()

# plt.boxplot(df["deforestation"])
# plt.show()

rgb_image = ipre_obj.rgb()

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.axis("off")
plt.savefig("/home/oscar/GitHub/BiOrbit_data/img_output/Deforestation.png",
            bbox_inches='tight', pad_inches=0)
# plt.show()

plt.imshow(rgb_image)
plt.axis("off")
plt.savefig("/home/oscar/GitHub/BiOrbit_data/img_output/RGB_image.png",
            bbox_inches='tight', pad_inches=0)
# plt.show()

img_def = cv2.imread('/home/oscar/GitHub/BiOrbit_data/img_output/Deforestation.png',
                     cv2.IMREAD_UNCHANGED)
img_rgb = cv2.imread("/home/oscar/GitHub/BiOrbit_data/img_output/RGB_image.png",
                     cv2.IMREAD_UNCHANGED)

final_img = cv2.addWeighted(img_def, 0.2, img_rgb, 1, 0)

cv2.imwrite('/home/oscar/GitHub/BiOrbit_data/img_output/final_img.png', final_img)
cv2.imshow('final_img', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

