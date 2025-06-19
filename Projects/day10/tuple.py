"""
元组
1. 元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销。
2. 元组是不可变类型，通常不可变类型在创建时间上优于对应的可变类型。
"""
t = ('wanyh', '32', True, '安徽合肥')

print(type(t)) # <class 'tuple'>
print(len(t)) # 4
print(t[1]) # 32
print(t[:3:2]) # ('wanyh', True)
print('32' in t) # True
print(t+t)

for elem in t:
    print(elem)

# 打包操作
a = 1,3,5
print(a) # (1, 3,5)
# 解包操作
i, j, k = a
print(i, j, k) # 1 3 5
m, *n = a
print(m, n) # 1 [3, 5]

# 交换变量使用到打包解包
a = 1
b = 2
c = 3
a, b, c = b, c, a
print(a, b, c) # 2, 3, 1

# 元组和列表转换
print(list(t)) # ['wanyh', '32', True, '安徽合肥']
print(tuple(list(t))) # ('wanyh', '32', True, '安徽合肥')
