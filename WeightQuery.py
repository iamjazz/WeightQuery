import requests
import re
import socket
import configparser
from concurrent.futures import ThreadPoolExecutor
config = configparser.ConfigParser()
config.read('./conf.ini',encoding='utf-8')
api = config.get("aizhan_api","api")
def wait():
    s =socket.socket()
    s.settimeout(1)
    #读取文件、过滤/字符
domains = [x.strip('/\n') for x in open('text.txt','r',encoding='utf-8').readlines()]
#去掉空格
print (domains)
ss = [br.strip() for br in domains]
#调用爱站网api
for br in ss:
    try:
        response = requests.get('https://apistore.aizhan.com/baidurank/siteinfos/'+api+'?domains='+br)
        m = re.search('"pc_br":(.+),"m_br',response.text).group(1)
        print ('域名：',br,'的权重是',m)
        wait()
        with open('{0}.txt'.format(m),'a+',encoding='utf-8') as a:#按权重分文件存储
            a.write(br)
            a.write('\n')

    except:
        continue
print('已完成，请在当前文件夹中查看')  