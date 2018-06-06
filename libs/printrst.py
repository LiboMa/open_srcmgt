import web
import requests
import subprocess

#rst=subprocess.Popen('curl -s --noproxy 127.0.0.1 http://127.0.0.1/srcmgt/opsapi?getrst=all_storage',shell=True,stdout=subprocess.PIPE).stdout.read()
rst=requests.get('http://127.0.0.1/srcmgt/opsapi?getrst=all_storage',proxies=None)


#print type(rst)

print rst
#for i in rst:
#    print i.eth1,i.eth0,i.project,i.gateway
