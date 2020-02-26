"""
获取对话的内容
"""
import urllib.request
import json
import time
import ssl
import string

def answer(message, key):
#   api_url = "http://openapi.tuling123.com/openapi/api/v2"
#   req = {
#       "perception":
#       {
#           "inputText":
#           {
#               "text": message
#           },
#
#           "selfInfo":
#          {
#               "location":
#               {
#                   "city": "石家庄",
#                    "province": "河北省",
#                   "street": "工农路"
#               }
#          }
#       },
#
#       "userInfo": 
#       {
#           "apiKey": key,
#           "userId": "387849"
#       }
#   }
    # print(req)
    # 将字典格式的req编码为utf8
#   req = json.dumps(req).encode('utf8')
    # print(req)

#   http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
#   response = urllib.request.urlopen(http_post)
#   response_str = response.read().decode('utf8')
    # print(response_str)
#   response_dic = json.loads(response_str)
    # print(response_dic)

#   intent_code = response_dic['intent']['code']
#   results_text = response_dic['results'][0]['values']['text']
    
    target = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    keyword = message
    tmp = target + keyword
    url = urllib.parse.quote(tmp, safe=string.printable)
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    res = json.loads(html)#json转为dict,json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型

    results_text = res['content']
    
    

    return results_text