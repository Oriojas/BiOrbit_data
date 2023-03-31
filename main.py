import json
import pickle
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import send_ipfs_data as s_ipfs
import deforestation_tend as deforest
from fastapi.encoders import jsonable_encoder
from fastapi import Header, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://ee5d-190-26-36-192.ngrok.io/docs

class Item(BaseModel):
    _protectedAreaId: int
    _protectedAreaName: str
    multiband: str

@app.post("/process_and_save_img/")
# async def process_and_save_img(metadata: dict, img_tif: str, date_reg: str, plot_name: str):
async def process_and_save_img(item: Item):
    print(item)
    # print(f"{img_tif.size}")
    # with open("temp_files/obj.pickle", "rb") as f:
    #     pickle.dump(img_tif, f)

    # print(type(img_tif))
    # data_process_obj = deforest.DataProcess(file_meta=metadata,
    #                                         ndvi_tif=img_tif)
    #
    # data_process_obj.process_meta(reg_date=date_reg,
    #                               view_plot=True,
    #                               log=True,
    #                               plot_name=plot_name)
    #
    # ipfs_obj = s_ipfs.PostIpfs(file_name=str(plot_name))
    #
    # cid_img, url_img = ipfs_obj.send_img()
    #
    # metadata = {"name": f"{plot_name}",
    #             "description": f"{plot_name} imagen con zonas rojas que indican deforestación",
    #             "image": f"{cid_img}"}
    #
    # with open(f"temp_files/{plot_name}.json", "w") as file:
    #     json.dump(metadata, file)
    #
    # cid_met, url_met = ipfs_obj.send_met(data=f"{plot_name}.json")
    #
    # cid_data = {"cid_nft_img": cid_img,
    #             "url_nft_img": url_img,
    #             "cid_json_data": cid_met,
    #             "url_json_data": url_met}
    #
    # json_output: object = jsonable_encoder(cid_data)
    #
    # return json_output
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)
