#python高级特性
#切片
l=['test1','test2','test3']
#从0开始,到2不包括2
print(l[1:2])
print(l[-2])
print(l[-2:])
l1=list(range(100))
print(l1[:])#所有
print(l1[::5])#每5个取一个
print((0, 1, 2, 3, 4, 5)[:3])#tuple切片操作还是tuple
print([0, 1, 2, 3, 4, 5][:3])
def trim(s):
    if s[0:1] == ' ':
        s=trim(s[1:])
    else:
        s = s
    if s[-1:] == ' ':
        s=trim(s[:-1])
    else:
        s = s
    return s
print(trim(' '))
#enumerate,迭代下标
for i,value in enumerate(['a','b','c']):
    print(i,value)
def find(L):
    if len(L)==0:
       return(None,None)
    max=L[0];
    min=L[0];
    for value in L:
       if value > max:
          max=value;
       if value <min :
          min=value
    return (min,max)
print(find([7]))
for i in (m+n for m in 'ABC' for n in 'abc'):
    print(i)
#isinstance(i,str) 判断i是否是str,是的话返回true
#L2 =[x.lower() for x in L1 if isinstance(x, str)]
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
print((m+n for m in 'ABC' for n in 'abc'))
print([m+n for m in 'ABC' for n in 'abc'])
def triangle():
    L1=[1]
    while True:
        yield L1
        L1=[1] + [L1[x]+L1[x+1] for x  in range(len(L1)-1)] + [1]
    return L1
results = []
n=0;
for t in triangle():
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
#类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
