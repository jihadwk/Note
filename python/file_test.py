#encoding=utf-8
#写文件 覆盖的方式,不存在文件，自动创建
f=open('test.txt','w')
f.write('first line\n')
f.write('next line\n')
f.close()
#读文件
f=open('test.txt','r')
#文件对象本身就是迭代器
for line in f :
    print line.rstrip()
f.close()

	