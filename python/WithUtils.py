
#　with 实现原理
# https://www.cnblogs.com/wanglei-xiaoshitou1/p/9238275.html

class Sample:

    def __init__(self,error):
        self.error = error
        print("init")

    def __enter__(self):
        print("enter")


    def __exit__(self, exc_type, exc_val, exc_tb):

        print("exit")
        print("exc_type:",exc_type)
        print("exc_val:",exc_val)
        print("exc_tb:",exc_tb)

        if self.error == exc_type:
            return True
        else:
            return False


def get_sample(error,*args,**kwargs):

    if args:
        if len(args) == 1:
            func = args[0]
            print(kwargs.keys())
            print(kwargs.values())
        else:
            func = args[0]
            try:
                func(*args[1:])
            except BaseException as exc:
                if not error == type(exc):
                    raise
    else:
        return Sample(error)


def test(a,b):
    return a/b

# 使用with测试

with get_sample(ValueError):
    raise ValueError

with get_sample(ZeroDivisionError):
    value = 3/0


# 使用func测试

get_sample(ValueError)

get_sample(ZeroDivisionError, test, 3, 0)

# get_sample(ZeroDivisionError, test, a=3, b=1)

# get_sample(ZeroDivisionError, lambda :3/0)











