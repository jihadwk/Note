#coding=utf-8
import httplib
#定义可以使用默认参数
#def check_web_server(host,port=80,path='/'):
def check_web_server(host,port,path):
	h=httplib.HTTPConnection(host,port)
	h.request('GET',path)
	resp = h.getresponse()
	print 'HTTP respone:'
	print '     status=',resp.status
	print '     reason=',resp.reason
	print 'HTTPHeaders:'
	for hdr in resp.getheaders():
	    print '     %s:%s'% hdr #hdr 是一个元组
check_web_server('www.python.org',80,'/')
#还可以这样调用：check_web_server(path='/',port='80',host='www.python.org')
print '%s:%s'%('t','test')	
#============
#匿名函数lambda
#============
lambda person: person.last_name
#python 里 *args:打开元组或列表和**kargs：打开字典， 支持变长参数

s='qq123se'
print s[:-1]
L = ['Michael', 100, True]
print L[:-1]
