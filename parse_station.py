import re
import requests
from pprint import pprint

#获取url
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9031'
response = requests.get(url,verify=False)   #这里为什么要加verify=False？   忽略对ssl证书的验证
#正则处理
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
pprint(dict(stations),indent=4)


