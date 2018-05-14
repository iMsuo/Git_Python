class test(object):
    def __init__(self,name,grade):#初始化函数
        self.__name=name
        self._grade=grade
    def getname(self):
        return  self.__name
    def setname(self,name):
        self.__name=name
    def setgrage(self,grade):
        self._grade=grade
    def  getgrade(self):
        return  self._grade
test1=test('hx',100)
print(test1.getname())
print(test1.getgrade())
test1.setname('hx1')
test1.setgrage(120)
print(test1.getname())
print(test1.getgrade())
#print(test1.__name)  私有变量
print(test1._grade)
print(isinstance(test1,test))
print(isinstance(test1,object))
print(type(123))
print(dir(test1))#获取方法
print('ABC'.__len__())
print(hasattr(test1,'_grade'))
setattr(test1,'_grade',11)
print(test1._grade)
#print(getattr(test1,'111'))
print(hasattr(test1,'getname'))
class student(object):
    name="hx"
stu1=student()
print(stu1.name)
print(student.name)
stu1.name='hx1'
print(stu1.name)
print(student.name)
del stu1.name
print(stu1.name)
print(student.name)
def set_age(self,age):
    self.age=age
from types import MethodType
test1.setage=MethodType(set_age,test1)
test1.setage(11)
print(test1.age)
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class students(object):
    def getscores(self):
        return self.__score
    @property
    def scores(self):
        return self.__score
    @scores.setter
    def scores(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value
stus1=students()#直接调用
stus1.scores=11
print(stus1.scores)
print(stus1.getscores())
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height=value
    @property
    def resolution(self):
        return  self.__height*self.__width
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
#MixIn python 支持多重继承