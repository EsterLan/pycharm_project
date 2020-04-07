# 键入关键字 采用bing搜索进行搜索
# 将返回的结果保存到一个网页文件

from urllib.request import urlopen, Request
from urllib import parse

key_word = input('>>Please enter the key world')
base_url = 'https://www.bing.com/search'
# 编码
data = parse.urlencode({
    'q': key_word
})
url = '{}?{}'.format(base_url,data)
print(url)

# 爬虫伪装
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
# 请求
req = Request(url, headers={
    'User-Agent': ua
})

# 返回类文件对象, 并写入网页文件
with urlopen(req) as response:
    with open('../bing_search.xml', 'wb+') as f:
        f.write(response.read())
        f.flush()
print('Sucess！')

