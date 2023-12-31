# Implementation of Global Variable and Local variable

x=10
def add(x):
    x=5
    x=x+10

    return x

print(add(10))
print(x)