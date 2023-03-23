import os
import json
import subprocess

KEY_EST = os.environ["KEY_EST"]
FOLDER_DATA = os.environ["FOLDER_DATA"]
FOLDER_JSON = os.environ["FOLDER_JSON"]


class PostIpfs:

    def __init__(self, file_name):

        self.file_name = file_name
        self.url = "https://api.estuary.tech/content/add"
        self.aut = f'"Authorization: Bearer {KEY_EST}"'
        self.con = '"Content-Type: multipart/form-data"'

    def send_img(self):

        dat = f'"data=@{FOLDER_DATA}/{self.file_name}.png"'

        post = f'curl -X POST {self.url} -H {self.aut} -H {self.con} -F {dat}'

        resp = subprocess.run(post,
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

    def send_met(self, data):

        dat = f'"data=@{FOLDER_JSON}/{data}"'

        post = f'curl -X POST {self.url} -H {self.aut} -H {self.con} -F {dat}'

        resp = subprocess.run(post,
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
