from sqlalchemy import create_engine
import pandas as pd
import os

#数据库连接
user = 'fanhaojie'
passwd = 'Chenfan@123'
host = '10.228.86.203'  ###正式机
port = 11101
dbname1 = 'test'
engine1 = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (user, passwd, host, port, dbname1))
for root, dirs, files in os.walk(r'D:\汇总数据'):
    img = pd.DataFrame(files,columns=['taobao_goods_id_jpg'])
    pd.io.sql.to_sql(img, 'taobao_img5g1', engine1, schema='test', if_exists='append')

