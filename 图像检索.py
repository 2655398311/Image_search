import re
from sqlalchemy import create_engine
from aip import AipImageSearch
import json
import os
import shutil
import pandas as pd
"""建立数据库连接"""
user='fanhaojie'
passwd='Chenfan@123'
host='10.228.86.203' ###正式机
port=11101
dbname1='test'
engine1 = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8"%(user,passwd,host,port,dbname1))
#百度IP池
# APP_ID = '17636858'
# API_KEY = 'OicrcYRGVtc8O9fiMjHFGNvY'
# SECRET_KEY = '9lfK9ircWbP2dZUu1yyg8mt6Gjf7OzUs'
a_id = [{'APP_ID':'17636858','API_KEY':'OicrcYRGVtc8O9fiMjHFGNvY','SECRET_KEY':'9lfK9ircWbP2dZUu1yyg8mt6Gjf7OzUs','score':500}]
#         {'APP_ID':'17617635','API_KEY':'xjta50dTzdyfSEYR7W4jtiuN','SECRET_KEY':'3YOiUPg1MBb7OpdvaDSZCqLmUPDS5H8R','score':500},
#         {'APP_ID':'17617658','API_KEY':'vbldDaPcXsMESWSHyMvfb5jG','SECRET_KEY':'aXLNxhfq7YvHwtK00EGLg3zBY5uY8Gmr','score':500},
#         {'APP_ID':'17619822','API_KEY':'OaYV9PQjAdpxkp5aZeqcdaeN','SECRET_KEY':'jdTKwjWmEfNhs6KAXioHqNivvPbDDSC8','score':500},
#         {'APP_ID':'17619843','API_KEY':'NM4HsWYPTGFjiG7wRqHb3MHm','SECRET_KEY':'o7u4up6VnuAhBC7x0s11AQz3DKA08SFU','score':500},
#         {'APP_ID':'17343743','API_KEY':'FFW1qWCqGBVebSlP6SC6y3a9','SECRET_KEY':'jcaan6O0ZLt2GS3x0auNLTEjrx8lDRYj','score':500},
#         {'APP_ID':'17636836','API_KEY':'kiHY1NZ1sC1bT6hFqMs2HCCE','SECRET_KEY':'hRNkLexmgfsxUDiNrg01YfCrs48i6qoy','score':500},
#         {'APP_ID':'17636858','API_KEY':'OicrcYRGVtc8O9fiMjHFGNvY','SECRET_KEY':'9lfK9ircWbP2dZUu1yyg8mt6Gjf7OzUs','score':500},
#         {'APP_ID':'17636955','API_KEY':'UV34UgsF1TqsLFRPXgMbakLB','SECRET_KEY':'NpM1WFy9C6ZdzfVt4T43jsPpMzTbQsR1','score':500}]
""" 你的 APPID AK SK """
# APP_ID = '17636858'
# API_KEY = 'OicrcYRGVtc8O9fiMjHFGNvY'
# SECRET_KEY = '9lfK9ircWbP2dZUu1yyg8mt6Gjf7OzUs'
# client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)

"""读取图片"""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""移动图片"""
def move_file(src_path, dst_path, file):
    f_src = os.path.join(src_path, file)
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    f_dst = os.path.join(dst_path, file)
    shutil.move(f_src, f_dst)

"""图片路径"""
src_path = r'D:\存在数据_result'
dst_path = r'D:\存在数据_result_1'
options = {}

data_list = []
"""调用相似图片检索"""
def jpg_jiansuo():
    for i in a_id:
        client = AipImageSearch(i['APP_ID'], i['API_KEY'], i['SECRET_KEY'])
        for root, dirs, files in os.walk(r'D:\api_diaoyong'):
            for file in files:
                re_result = re.match('(\d+)', file)
                if re_result:
                    aa = re_result.group(1)
                options["tags"] = "100,11"
                options["tag_logic"] = "0"
                options["pn"] = "100"
                options["rn"] = "250"
                a = client.similarSearch(get_file_content(os.path.join(root, file)), options)
                print(a)
                # print(a)
                # i['score'] -= 1
                # if i['score'] > 0:
                #     move_file(src_path, dst_path, file)
                #     a_data = pd.DataFrame(a['result'])
                #     a_data['taobao_goods_id'] = aa
                    # a_data.to_excel('jiansuo.xlsx')
                    # pd.io.sql.to_sql(a_data, 'photo1', engine1, schema='test', if_exists='append')
                # else:
                #     pass

                # data_list.append(pd.DataFrame(a['result']))


if __name__ =='__main__':
    jpg_jiansuo()
