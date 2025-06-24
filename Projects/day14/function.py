"""
函数
"""
import module as m1

def sum(a, b):
    return a + b

print(sum(3, 4))

# 可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add(1,2,3,4))

# 传入字典
def foo(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

foo(name='wany', age=32)

# 用模块管理函数
print(m1.sum(1, 2, 3))