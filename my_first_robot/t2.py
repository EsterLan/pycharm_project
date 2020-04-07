# from urllib import parse

# d = {
#     'id': 0,
#     'name': 'ester'
# }

# url = 'http://www.magedu.com/python?id=0&name=ester' #GET

# url = 'http://www.magedu.com/python' # POST
# body 'id=0&name=ester'
# url = 'http://www.magedu.com/python'
# url编码
# u = parse.urlencode(d)
# print(u)

# 网页采用utf-8编码
# https://www.baidu.com/s?wd=中
# url编码后上述
# https

from urllib import parse

u = parse.urlencode({'wd': '中'}) # 搜索内容进行编码
url = 'https://www.baidu.com/s?'.format(u) #将参数部分与待搜索进行拼接
print(url)
print('中'.encode('utf-8')) # b'\xe4\xb8\xad'

print(parse.unquote(u)) # 解码
print(parse.unquote(url))



