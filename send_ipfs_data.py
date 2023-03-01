import os
import json
import subprocess

KEY_EST = os.environ["KEY_EST"]
FOLDER_DATA = os.environ["FOLDER_DATA"]


class postIpfs:

    def __init__(self, file_name):

        self.file_name = file_name
        url = "https://api.estuary.tech/content/add"
        aut = f'"Authorization: Bearer {KEY_EST}"'
        con = '"Content-Type: multipart/form-data"'
        dat = f'"data=@{FOLDER_DATA}/{self.file_name}.npz"'

        self.post = f'curl -X POST {url} -H {aut} -H {con} -F {dat}'

    def send_data(self):
        resp = subprocess.run(self.post,
                              stderr=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              text=True,
                              shell=True)

        try:
            dict_resp = json.loads(resp.stdout)

            cid = dict_resp.get('cid')
            ret_url = dict_resp.get('retrieval_url')

        except:

            cid = "Bad Request"
            ret_url = "Bad Request"

        return cid, ret_url