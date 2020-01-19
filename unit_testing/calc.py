def add(x, y):
    """Add Function"""
    for i in (x,y):
        if not (isinstance(i,int) or isinstance(i,float)):
            raise ValueError('argument is not a number')
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
