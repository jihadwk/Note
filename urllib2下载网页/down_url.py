#-*- coding utf-8 -*-
import urllib2
#ֱ������
respone = urllib2.urlopen('http://www.baidu.com')
#��ȡ״̬�룬�����200��ʾ��ȡ�ɹ�
print respone.getcode()
#��ȡ����
cont = respone.read()

