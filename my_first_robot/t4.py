# post方法
# 将data写到测试网站http://httpbin.org/post中

from urllib.request import urlopen, Request
from urllib import parse
import json

# url = 'http://httpbin.org/post' #POST
# data = parse.urlencode({'name': 'ester', 'field':'punk'}) # body
# print(data)
# # 身份伪装
# ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
# # 加入请求头
# req = Request(url, headers={
#     'User-Agent': ua
# })
#
# with urlopen(req, data.encode()) as response:
#     # POST请求， data不为None
#     # data内容应当进行url编码，安全性
#     # data编码为字符， urlopen接受的为bytes?
#     text = response.read()
#     # simplejson可自动对bits或bytes进行转换为json
#     d = json.loads(text)
#     # 实际中返回的数据，网站不一定采用json，实际需要测试
#     print(d)
#     print(type(d))

# GET请求
base_url = 'https://www.bing.com'
u = {
    'q': 'stella maxwell'
}
# 关键字进行url编码
key_word = parse.urlencode(u)
print(key_word)
# 拼接url
# 字符串的写法规范: +和%的使用
url = '{}/search?{}'.format(base_url, key_word)

# 伪装User-Agent
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
# 将其加入请求头
req = Request(url, headers={
    'User-Agent': ua
})

# 将urlopen()返回的类文件对象写入网页文件, 保存到本地
with urlopen(req, data=None) as response:
    with open('./stella_maxwell.xml', 'wb+') as f:
        f.write(response.read())
        f.flush()


