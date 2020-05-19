from aip import AipImageSearch
from sqlalchemy import create_engine
""" 你的 APPID AK SK """
APP_ID = '19413368'
API_KEY = 'z9Blx6giRyn3MVOwIg7xBEdu'
SECRET_KEY = 'spnwrGf0Pih5KTG2sCWMEZmGUTke9C7K'
user='fanhaojie'
passwd='Chenfan@123'
host='10.228.86.203' ###正式机
port=11101
dbname1='test'
engine1 = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"%(user,passwd,host,port,dbname1))
client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
import os

options = {}
import random
import time
import pandas as pd
for root, dirs, files in os.walk(r'D:\picture_all_April'):
    bb = []
    for file in files:
        print(file)
        a = time.time()
        options["brief"] =file
        options["tags"] = "100,11"
        aa_result = client.similarAdd(get_file_content(os.path.join(root, file)), options)
        bb.append(aa_result)
    bb_content_sign = pd.DataFrame(bb)
    print(bb_content_sign)
    pd.io.sql.to_sql(bb_content_sign, 'april_cont_sign', engine1, schema='test', if_exists='append')

# image = get_file_content('O1CN010vAmBL1ntpVDABFQq_!!791105148.jpg')
# """ 调用相似图检索—入库, 图片参数为本地图片 """
# client.similarAdd(image)
""" 如果有可选参数 """


""" 带参数调用相似图检索—入库, 图片参数为本地图片 """
# client.similarAdd(image, options)

# url = "http//www.x.com/sample.jpg"
#
# """ 调用相似图检索—入库, 图片参数为远程url图片 """
# client.similarAddUrl(url)

# """ 如果有可选参数 """
# options = {}
# options["brief"] = "兔八哥"
# options["tags"] = "100,11"
#
# """ 带参数调用相似图检索—入库, 图片参数为远程url图片 """
# client.similarAddUrl(url, options)
# O1CN01Ci2g1u1ntpQPVfBfQ_!!791105148
# O1CN01CDoH951ntpVA9KiMa_!!791105148