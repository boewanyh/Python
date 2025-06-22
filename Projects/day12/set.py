"""
集合
"""
# 创建集合
set1 = {'apple', 'banana', 'grape', 'apple'}
print(set1) # {'banana', 'apple', 'grape'}  元素不可重复
set2 = set([1, 2, 3, 3, 4])
print(set2) # {1, 2, 3, 4}

# 遍历
for elem in set1:
    print(elem)

# 成员运算
print('apple' in set1)
print('apple' not in set1)

# 二元运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2) # 交集 {3, 4}
print(set1.intersection(set2))
print(set1 | set2) # 并集 {1, 2, 3, 4, 5, 6}
print(set1.union(set2))
print(set1 - set2) # 差集 {1, 2}
print(set1.difference(set2))
print(set1 ^ set2) # 对称集 {1, 2, 5, 6}
print(set1.symmetric_difference(set2))
set1 |= set2
# set1.update(set2)
print(set1) # {1, 2, 3, 4, 5, 6}
set1 = {1, 2, 3, 4}
set1 &= set2
# set1.intersection_update(set2)
print(set1) # {3, 4}
set1 = {1, 2, 3, 4}
set1 -= set2
# set1.difference_update(set2)
print(set1) # {1, 2}

# 比较运算
set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
print(set1 < set2) # True 真子集
print(set1 <= set2) # True 子集
print(set1.issubset(set2))
print(set2 > set1) # True 超集
print(set2.issuperset(set1))
print(set2 == set3) # True

# 集合方法
set1 = {1, 2, 3, 4}
set1.add(5) # 添加元素
set1.discard(1) # 删除元素
set1.remove(2) # 不存在 KeyError
print(set1)
set1.clear() # 清空

# 是否有相同元素
set1 = {1, 2}
set2 = {2, 3}
set3 = {4, 5}
print(set1.isdisjoint(set2)) # False
print(set1.isdisjoint(set3)) # True

# 不可变集合
set = frozenset({1, 3, 5, 7})
print(set)