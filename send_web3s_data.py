import os
import json
import traceback
import subprocess
from sys import exc_info

ERR_SYS = "System error: "

KEY_WEB3 = os.environ["KEY_WEB3"]
FOLDER_DATA = os.environ["FOLDER_DATA"]


class postIpfsW3:

    def __init__(self, file_name):

        self.file_name = file_name
        url = '"https://api.web3.storage/upload"'
        acc = '"accept: application/json"'
        aut = f'"Authorization: Bearer {KEY_WEB3}"'
        con = '"Content-Type: multipart/form-data"'
        nam = f'"X-NAME: {file_name}"'
        fil = f'"file=@{FOLDER_DATA}/{self.file_name}.npz"'

        self.post = f'curl -X POST {url} -H {acc} -H {aut} -H {con} -H {nam} -F {fil}'

    def send_data(self):
        resp = subprocess.run(self.post,
                              stderr=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              text=True,
                              shell=True)

        try:
            dict_resp = json.loads(resp.stdout)

            cid = dict_resp.get('cid')
            carCid = dict_resp.get('carCid')

        except Exception as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(''.center(60, '='))
            traceback.print_exc()

            cid = "Bad Request"
            carCid = "Bad Request"

        return cid, carCid
