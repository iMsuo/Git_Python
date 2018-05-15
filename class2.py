class test1(object):
    __slots__=('name','age')#限制只能初始化name和age
    def __str__(self):#用于
        return 'name:%s,age:%s'%(self.name,self.age)
    __repr__=__str__
    def __iter__(self):
        return self
    def __next__(self):
        self.name,self.age=self.name,self.age+1
        if self.age==100:
            raise StopIteration()
        return  self.name,self.age
    def __getitem__(self, item):
        a,b=1,1
        if isinstance(item,int):
            for x in range(item):
                a,b=a,b+a
            return b
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            l=[]
            for x in range(stop):
                if(x>=start):
                    l.append(b)
                a,b=a,b+a
            return l
    def __getattr__(self, item):#只有没有这个属性才会调用
        if item=='score':
            return  lambda:100;
test11=test1()
test11.name='hx'
test11.age=24
print(test11)
for n in test11:
    print(n)
print(test11[2])
print(test11[2:5])#切片
#test11.ss=11
print(test11.score())

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)
#chain()第一次调用，__path为'',之后找参数没有，就调用__getattr__，之后调用chain（.....），租后返回一个string （repr# ）
#callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(test1))

print("____________________________")
from enum import Enum,unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,',',member,',',member.value)
@unique
class week(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
def fn(x):
    return x
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
Hello1=type('Hello',(object,),dict(hello=fn))
t1=Hello1()
type(t1)
t1.hello()



