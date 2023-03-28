import send_web3s_data as s_web3

FILE_NAME = "img"

cid = s_web3.postIpfsW3(file_name=str(FILE_NAME)).send_data()

print(f"{cid}")
