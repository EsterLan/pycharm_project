from urllib.request import urlopen, Request
import random
'''

'''

# url = 'http://www.bing.com'
url = 'https://www.douban.com/j'
# ua_list 来对爬虫进行伪装
# ua_list =['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36' # chrome on Ubuntu
#           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36' # chrome on X11
#           ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36Edge/13.10586'# edge
          # ]

# ua = random.choice(ua_list) # 随机pick一个ua进行伪装
# 将ua加到request header中
ua = 'Mediapartners-Google'
req = Request(url)
req.add_header('User-Agent', ua)
print(type(req))

response = urlopen(req, timeout=5)
print(type(response))

# 对类文件进行操作
with response:
    print(1, response.status, response.reason) # 返回状态
    print(2, response.info()) # 返回响应头headers
    print(3, response.read()) # 返回读取内容
    print(4, response.geturl()) # 返回数据的url，如果重定向，这个url与原始url不同
    # 如原始‘http://www.bing.com’, 返回‘https://cn.bing.com’

print(5, req.get_header('User-agent'))