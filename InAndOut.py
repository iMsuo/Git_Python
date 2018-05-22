try:
    f = open('E:/JAVA/1.txt', 'rb')
    print(f.read())
finally:
    if f:
        f.close()
print("--------------")
#简洁写法
print("r--------------")
with open('E:/JAVA/1.txt','rb') as f:
    print(f.read())
print("rb--------------")
with open('E:/JAVA/1.txt','rb') as f:
    print(f.read())
print("---------")
try:
    f=open('E:/Java/1.txt','r',encoding='gbk',errors='ignore')
    print(f.read())
finally:
    if f:
        f.close()
try:
    f=open('E:/Java/1.txt','w')
    f.write("hello world!")
finally:
    if f:
        f.close()
with open('E:/JAVA/1.txt','rb') as f:
    print(f.read())
print('=========StringIO')
from io import StringIO
f=StringIO()
f.write("hello ")
f.write("\n")
f.write('world')
print(f.getvalue())
f.close()
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
print('=========os文件')
import os
print(os.name)
print(os.path.abspath('.'))
print(os.path.join('E:\JAVA\Python\Git_Python','testdir'))
#os.mkdir(os.path.join('E:\JAVA\Python\Git_Python','testdir.txt'))
#os.rmdir(os.path.join('E:\JAVA\Python\Git_Python','testdir'))
print(os.path.split(os.path.join('E:\JAVA\Python\Git_Python','testdir.txt')))
for x in os.path.split(os.path.join('E:\JAVA\Python\Git_Python','testdir.txt')):
    print(x)
print(os.path.splitext(os.path.join('E:\JAVA\Python\Git_Python','testdir.txt')))
#os.rename('E:/JAVA/Python/Git_Python/testdir.txt','E:/JAVA/Python/Git_Python/testdir.py')

#Iscomplete=False
#while not Iscomplete:
#    dir=input("input:")
#    Iscomplete=(os.path.exists((dir)) and os.path.isdir(dir))
#    if Iscomplete:
#        break
#    else:
#        print("error")

def search(dir):
    files=os.listdir(dir)
    opath=os.path
    for file in files:
        fullpath=opath.join(dir,file)
        if opath.isdir(fullpath):
            search(fullpath)
        if opath.isfile(fullpath):
            name=opath.split(fullpath)[1]
            print(fullpath)

#search(dir)

print('----------序列化')
import pickle
d=dict(name='hx',age=23)
f=open('E:/JAVA/1.txt','wb')
pickle.dump(d,f)
f.close()
f=open('E:/JAVA/1.txt','rb')
d=pickle.load(f)
f.close()
print(d)
print('==========json')
import json
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

stdudent1=student('hx',23)

def studentToJson(stu):
    return {
        'name':stu.name,
        'age':stu.age
    }
print(json.dumps(stdudent1,default=studentToJson))
print(json.dumps(stdudent1,default=lambda obj:obj.__dict__))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)





