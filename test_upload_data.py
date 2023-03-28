import json
import send_ipfs_data as s_ipfs

FILE_NAME = "final_img"

ipfs_obj = s_ipfs.PostIpfs(file_name=str(FILE_NAME))

cid_img, url_img = ipfs_obj.send_img()

print(f"Imagen: CID: {cid_img}, URL: {url_img}")

metadata = {"name": f"{FILE_NAME}",
            "description": "Parque Nacional Natural Selva de Florencia",
            "image": f"{cid_img}"}

with open(f"temp_files/{FILE_NAME}.json", "w") as file:
    json.dump(metadata, file)

cid_met, url_met = ipfs_obj.send_met(data=f"{FILE_NAME}.json")


print(f"Metadata: CID: {cid_met}, URL: {url_met}")
