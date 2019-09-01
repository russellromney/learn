import functools

def my_decorator(func):
    @functools.wraps(func)
    def runs_func():
        print('within decorator')
        func()
        print('after decorator')
    return runs_func

@my_decorator
def my_function():
    print('i am the function')

#my_function()

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def runs_func(*args, **kwargs):
            if number == 56:
                print('not running the function')
            else:    
                print('in the decorator')
                func(*args, **kwargs)
                print('after the decorator')
        return runs_func
    return my_decorator

@decorator_with_arguments(55)
def my_function_too(x,y):
    print(x+y)

my_function_too(57,78)