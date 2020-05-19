import requests
from flask import Flask, request, jsonify, abort
import os
from uuid import uuid4

from april_jiansuo import jpg_jiansuo_api
#jpg_jiansuo_api = lambda:[1]

app = Flask(__name__)


cur_dir = os.path.dirname(os.path.abspath(__file__))
image_save_dir = os.path.join(cur_dir, 'upload_images')

if not os.path.exists(image_save_dir):
    os.makedirs(image_save_dir)


xiang_shi_kuan_dir = os.path.join(cur_dir, "相似款1")
if not os.path.exists(xiang_shi_kuan_dir):
    raise Exception(f"path {xiang_shi_kuan_dir} not exsit")

class XiangShiKuan(object):
    def __init__(self, image_dir_name, suffixs = ('.jpg', '.png')):
        files = os.listdir(image_dir_name)
        #files = filter(lambda x: os.path.isfile(x), files)
        files = list(filter(lambda x: any(x.endswith(suffix) for suffix in suffixs), files))

        self.names = set(files) # 相似图片名称，没去掉后缀名的

        
xiang_shi_kuan_List = []
for dirx in os.listdir(xiang_shi_kuan_dir):
    dir_ = os.path.join(xiang_shi_kuan_dir, dirx)
    if os.path.isdir(dir_):
        image_dir_name = os.path.join(xiang_shi_kuan_dir, dir_)  
        xiang_shi_kuan_List.append(XiangShiKuan(image_dir_name))

xiang_shi_kuan_Set = set()
for xiang_shi_kuan in xiang_shi_kuan_List:
    xiang_shi_kuan_Set.update(xiang_shi_kuan.names)



TOKENS = {'68b848b7-d760-47d1-abb9-a5cddd62470e'}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36"
}


def save_image(image_name, image_content, save_dir=image_save_dir):
    image_abs_path = os.path.join(save_dir, image_name)
    with open(image_abs_path, 'wb') as f:
        f.write(image_content)


def gen_image_name(suffix='.jpg'):
    seq = str(uuid4())
    return seq + suffix


def get(url, times=5):
    for _ in range(times):
        try:
            r = requests.get(url, headers=headers)
            return True, r
        except:
            pass
    return False, None


@app.route("/api/jiansuo", methods=['POST'])
def jiansuo():
    data = request.get_json()

    r_token = data.get('TOKEN', None)
    if r_token == None or r_token not in TOKENS:
        abort(400)

    image_name = data.get("file", None)
    if image_name != None and image_name in xiang_shi_kuan_Set:
        for xiang_shi_kuan in xiang_shi_kuan_List:
            if image_name in xiang_shi_kuan.names:
                names = filter(lambda x: x != image_name, xiang_shi_kuan.names)
                suffixs = ('.jpg', '.png')
                briefs = []
                for name in names:
                    tem = name
                    for suffix in suffixs:
                        tem = tem.strip(suffix)
                    briefs.append(tem)
               # briefs = briefs[:15]
                return_data = {'top_n': briefs}
                return_data.update(code=200)
                return jsonify(return_data)
                                
    url = data.get('url', None)
    if url == None:
        abort(400)

    status, r = get(url)

    if status == True:
        image_name = gen_image_name()
        save_image(image_name, r.content)

        datas = jpg_jiansuo_api(r.content)
        briefs = list(map(lambda x: x.strip('.jpg'),
                          map(lambda x: x['brief'], datas)))
                          
        return_data = {'top_n': briefs}
        return_data.update(code=200)
        return jsonify(return_data)
    else:
        return_data = dict()
        return_data.update(status=f"get url:{url} failed")
        return jsonify(return_data)


if __name__ == "__main__":
    app.run("0.0.0.0", port=9080, debug=True)
