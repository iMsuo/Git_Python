#函数式编程
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#变量可以指向函数。
from functools import reduce
f=abs
print(f(-22))
def f1(x):
    return x*x;
for i in map(f1,[2,3,4]):
    print(i)
print([i for i in map(f1,[2,3,4])] )
print((i for i in map(f1,[2,3,4])) )#generator生成器
#reduce把结果继续和序列的下一个元素做累积计算
def sum1(x,y):
    return x+y
print(reduce(sum1,[1,2,3]))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strToList(s):
    return DIGITS[s]
def strToInt(x,y):
    return x*10+y
print(i for i in map(strToList,"12345"))
print(reduce(strToInt,map(strToList,"12345")))
#map会将传递进去的值变成iterator，一个一个地进行处理
#reduce把结果继续和序列的下一个元素做累积计算
def normalize(name):
    return name[0:1].upper() + name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
def str2float(s):
    s1=s.split('.')
    def f1(x1,y1):
        return x1*10+y1
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def f3(x3):
        return DIGITS[x3]
    return reduce(f1,map(f3,s1[0]))+reduce(f1,map(f3,s1[1]))/(10**len(s1[1]))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
def is_palindrome(n):
    return str(n)[0:]==str(n)[::-1]#[::-1]表示倒置
#fileter 过滤器 filter（方法，list）
for i in range(5):
    print(i)
def count():
    def f(j):
        def g():
            return j * j

        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1=count()
f2=count()
print('------------')
print(f1)
for i in f1:
    print(i())
for i in f2:
        print(i())
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#@functools.wraps(func)    result = func(*args,**kw)
#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
#int2 = functools.partial(int, base=2)