"""
函数
"""
import operator
import functools
# 高阶函数
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

print(calc(0, operator.add, 1, 2, 3, a=4))
print(calc(1, operator.mul, 1, 2, 3, a=4))

# Lambda函数
fac = lambda n: n * n
print(fac(10))

# 偏函数
int2 = functools.partial(int, base=2)
print(int2('1001'))