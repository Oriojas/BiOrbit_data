import cv2
import json
import numpy as np
import pandas as pd
import img_prepare as ipre
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score


class DataProcess:

    def __init__(self, file_meta: str, ndvi_tif: str):

        self.file_meta = file_meta
        self.ndvi_tif = ndvi_tif

    def process_meta(self, reg_date: str, view_plot: bool = False, log: bool = False, plot_name: str = "plot_tend"):

        with open(self.file_meta, 'r') as f:
            m_data = json.load(f)

        dict_df = {"date": m_data["detection_date_list"],
                   "deforestation": m_data["total_extension_forest_cover_list"]}

        df_meta = pd.DataFrame.from_dict(dict_df)
        df_meta["date"] = df_meta["date"].apply(lambda x: x[0:10])
        df_meta["date"] = pd.to_datetime(df_meta["date"])
        x_train = np.array(df_meta["date"].apply(lambda x: pd.to_datetime(x).timestamp()))
        x_train = x_train.reshape(-1, 1)

        y_train = np.array(df_meta["deforestation"])

        regr = linear_model.LinearRegression()
        regr.fit(x_train, y_train)
        y_pred = regr.predict(x_train)
        df_meta["pred"] = y_pred

        dict_pre = {"date": pd.to_datetime(reg_date),
                    "deforestation": regr.predict(np.array(pd.to_datetime(reg_date).timestamp()).reshape(-1, 1)),
                    "pred": regr.predict(np.array(pd.to_datetime(reg_date).timestamp()).reshape(-1, 1))}

        df_meta_pred = pd.DataFrame.from_dict(dict_pre)
        df_meta = pd.concat([df_meta, df_meta_pred])

        plt.plot(df_meta["date"].iloc[0:-1], df_meta["deforestation"].iloc[0:-1], "-o", label="deforestation")
        plt.plot(df_meta["date"], df_meta["pred"], "--", label="projection")
        plt.hlines(y=m_data["total_extension_protected_area"],
                   xmin=df_meta["date"].min(), xmax=df_meta["date"].max(),
                   label="total_area", color="green")

        plt.title(f"Deforestation: {m_data['protected_area_name']},"
                  f"R2={round(r2_score(df_meta['deforestation'], df_meta['pred']), 2)}")
        plt.legend(loc='lower right')
        if log:
            plt.yscale("log")
        plt.grid()
        if view_plot:
            plt.show()
        plt.savefig(f"/home/oscar/GitHub/BiOrbit_data/plots/{plot_name}_boxp.png")

        plt.boxplot(df_meta["deforestation"])
        if view_plot:
            plt.show()
        plt.savefig(f"/home/oscar/GitHub/BiOrbit_data/plots/{plot_name}_reg.png")

        print("Regression OK")

    def process_ndvi_tif(self, view_plot: bool = False):

        ipre_obj = ipre.ImgPrepare(file_path=self.ndvi_tif)
        _, _, data = ipre_obj.prepare()

        rgb_image = ipre_obj.rgb()
        plt.imshow(data, cmap='hot', interpolation='nearest')
        plt.axis("off")
        plt.savefig("/home/oscar/GitHub/BiOrbit_data/img_output/Deforestation.png",
                    bbox_inches='tight', pad_inches=0)
        if view_plot:
            plt.show()

        plt.imshow(rgb_image)
        plt.axis("off")
        plt.savefig("/home/oscar/GitHub/BiOrbit_data/img_output/RGB_image.png",
                    bbox_inches='tight', pad_inches=0)
        if view_plot:
            plt.show()

        img_def = cv2.imread('/home/oscar/GitHub/BiOrbit_data/img_output/Deforestation.png',
                             cv2.IMREAD_UNCHANGED)
        img_rgb = cv2.imread("/home/oscar/GitHub/BiOrbit_data/img_output/RGB_image.png",
                             cv2.IMREAD_UNCHANGED)

        final_img = cv2.addWeighted(img_def, 0.2, img_rgb, 1, 0)

        cv2.imwrite('/home/oscar/GitHub/BiOrbit_data/img_output/final_img.png',
                    final_img)

        if view_plot:
            print("Press 0 for close window")
            cv2.imshow('final_img', final_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        print("Process img OK")
