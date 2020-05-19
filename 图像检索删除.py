
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 调用删除相同图，图片参数为远程url图片 """
client.sameHqDeleteByUrl(url)

contSign = "8cnn32frvrr2cd901"

""" 调用删除相同图，传入参数为图片签名 """
client.sameHqDeleteBySign(contSign)