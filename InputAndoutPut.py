#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#We choose # to note 
#Python 大小写敏感
#转义字符\
#r''表示内容默认不转义
#'''...'''表示多行
#bool值True 和False 。运算符and,or,not,空值None
# /值为浮点数，//除数取整
#ord 获取字符整数表示，chr把编码转化为对应的字符
#%%来表示一个%
#tuple(())于list([])类似,tuple一旦初始化就不能改变
#input读取的值是string，转化int(str)
#range(5)生成的序列是从0开始小于5的整数：
#str是不变对象，而list是可变对象。
name=input()
print('Hello',name)
print('I will tell you : 1024*768 = ',1024*768)
a=1000
if a>=100:
	print(a)
else:
	print(-a)
print("\"test\"")
print("I\'m \n OK")
print(r"\n\t\\\\")
print('''line1
...line2
...line3''')
if a==100:
	print('a=100')
else:
	print('a!=100')
print('\'Hello,world\'')
print('Hello,\\\'Adam\'\'')
print(r'Hello,"Bart"')
print(ord('A'))
print(chr(88))
print(b'ABC')
print(b'ABC'.decode('ascii'))
print(len('ABC'))
print(len(b'ABC'))
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
print(len('ABC'.encode('ascii')))
print(len('ABC'.encode('utf-8')))
print("%d%s"%(1,'hx'))
print("%d"%1)
print("{0}{1:.1f}".format('hx',1.1))
classmates=['test1','test2','test3']
print(classmates)
print(classmates[-1])
classmates.append('test4')
print(classmates)
classmates.insert(1,"newtest1")
classmates.pop(2)
print(classmates)
age=17
if age>=18:
	print('OK')
	print("ADULT")
elif age>16:
	print('Senior')
else:
	print("NG")
	print("Child")
#字典
dic={"test1":11,'test2':22,'test3':33}
print(dic['test2'])
print('test4' in dic)
set1=set([1,2,2,2,2,3])
print(set1)