"""
def add(a, b):
    return a+b
def sub(a, b):
    return a-b

print(add(1,4))
print(sub(4,2))
"""
def positive(x) :
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))