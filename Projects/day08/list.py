"""
列表
"""
# 创建列表
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = list('hello')
items3 = list(range(1, 10))
print(items1)
print(items2)
print(items3)

# 列表运算
items4 = items1 + items2 # 拼接
items5 = items1 * 2 # 重复
print(items4)
print(items5)
print(items1 == items2)

# 判断元素是否在列表中
print(99 in items1)
print(99 not in items1)

# 访问列表元素
print(items1[0])
print(items1[-1])
items1[0] = 10
print(items1)
print(items1[1:5:2]) # [start:end:stride] 终止位置的元素无法访问
items1[1:3] = [20, 30]
print(items1)

#遍历列表
for item in items1:
    print(item)