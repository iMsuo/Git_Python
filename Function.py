print("Function")
print(abs(-10))
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
print(my_abs(-22))
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(2))
def add_end(L=[]):
    L.append("END")
    return L
print(add_end())
print(add_end())
#list 是可变对象 []
#tuple是不可变对象（）但是无法操作
#def add_end1(L=()):
#    L.append("END")
#    return L
#print(add_end1())
#print(add_end1())
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end2())
print(add_end2())
def cal(numer):
    sum=0
    for n in numer:
        sum=sum+n
    return  sum
print(cal([1,2,3]))
#前面加个*可以不用将输入转化为list或tuple
def cal1(*numer):
    sum=0
    for n in numer:
        sum=sum+n
    return  sum
print(cal1(1,2,3))
#一个星（*）：表示接收的参数作为元组来处理
#两个星（**）：表示接收的参数作为字典来处理
def cal2(**number):
    for name,value in number.items():
        print(name,value)
cal2(test1="t1",test2='t2')
#*，表示后面的参数只能是
def person(name,age,*,city,job):
    print("name:",name,"age:",age,"city:",city,'job:',job)
person('hx',24,city='NT',job='PG')
#已定义了一个args，后面就不需要*，直接写就行了
def person1(name,age,*args,city,job):
    print("name:", name, "age:", age, "city:", city, 'job:', job)
person1('hx',24,city='NT',job='PG')
##使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def test1(a,b,c,*d,**e):
    print('a:',a,'b:',b,'c:',c,'d；',d,'e:',e)
tu=(1,2,3,4,5)
dic1={'t1':'t1','t2':'t2'}
test1(*tu,**dic1)
#使用递归函数的时候可能出现栈溢出，解决方法使用尾递归，即递归函数不包括表达式
#eg:汉诺塔的移动可以用递归函数非常简单地实现
#编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
#递归要用递归的思路去想，如果用一个一个的去想，相出一个共通是很难解决的
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
move(3, 'A', 'B', 'C')