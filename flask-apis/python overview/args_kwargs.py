def my_method(arg1,arg2):
    return arg1+arg2
my_method(3,4)

def my_long_method(*args,**kwargs):
    return sum(args)-sum(kwargs.values())

print(my_long_method(1,2,3,4,5,6,7,8,this=36))

