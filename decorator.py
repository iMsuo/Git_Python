def decoratortest1(fun):
    def wrapper():
        print("head")
        fun()
        print("foot")
    return  wrapper#注意这里是没有括号的，还有是主函数返回的

@decoratortest1
def show():
    print("body");

show()

def decoratortest2(fun):
    def wrapper(a,b):
        print("head2")
        fun(a,b)
        print("foot2")
    return  wrapper#注意这里是没有括号的，还有是主函数返回的

@decoratortest2
def show1(a,b):
    print("body",a,b);

show1('t1','t2')

print('--------------')
def decoratortest3(fun):
    def wrapper1(*args,**kwargs):
        def wrapper():
            fun(*args,**kwargs)
            return wrapper
        print("head3")
        wrapper()
        print("foot3")
    return  wrapper1#1注意这里是没有括号的，还有是主函数返回的
@decoratortest3
def show2(func,func1):
    func();
    func1('t1','t2');
    print("body3");

show2(show,show1)

