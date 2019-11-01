import requests
import numpy as np
import pandas as pd
import json
import time

# 头部与请求信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /'
                         'Chrome/77.0.3865.90 Safari/537.36'}
list_data = {'show_type': '3',
'type': '1',
'size': '2000',
'page': '1'
        }
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# 获取用户详细信息
def getDetail(bd_list,result):
    for a in bd_list:
        try:
            detail_data = {
                'b_id': '%s' % a
            }
            # print(detail_data)
            bd_res = requests.post('https://zhishuapi.aldwx.com/Main/action/Business/Business_api/DetailBusiness',headers=headers, data=detail_data)
            data = pd.DataFrame(json.loads(bd_res.text)['data'], index=[0])
            print(data)
            result = result.append(data, ignore_index=True)
            print(len(result))
        except:
            print("数据获取异常，异常id为{}".format(a))
        continue
    return result


# 获取小程序bd_id
def getBd_id():
    res = requests.post('https://zhishuapi.aldwx.com/Main/action/Business/Business_api/ListBusiness', headers=headers,
                        data=list_data)
    bd_data = pd.DataFrame(json.loads(res.text)['data'])
    bd_id = list(bd_data['id'])
    # print(bd_id[:50])
    return bd_id

result = pd.DataFrame()
bdid_list = getBd_id()
# print(bdid_list)
alddata = getDetail(bdid_list,result)
doc = pd.ExcelWriter('{}阿拉丁明细数据2.xlsx'.format(date))
alddata.to_excel(doc,na_rep='')
doc.save()
