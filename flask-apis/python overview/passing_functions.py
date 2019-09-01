def methodception(another):
    return another()

def add_():
    return 35+77

print(methodception(lambda: 35+66))

l = [1,2,3,4,4,13]
print(list(filter(lambda x : x != 13, l)))

print((lambda x : x*2)(4))

def not13(x):
    return x!=13
print(list(filter(not13,l)))