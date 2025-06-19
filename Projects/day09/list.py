"""
列表
"""
import random

languages = ['Python', 'Java', 'C#']

# 添加和删除
languages.append('C++')
languages.insert(1, "C")
print(languages)
languages.remove('Java') # 移除第一个'Java'
languages.pop()
languages.pop(1)
print(languages)
languages.clear()

# 元素位置和频次
items = ['Python', 'Java', 'Java', 'C#', 'Python']
print(items.index('Python', 1)) # 从索引位置1开始查找'Python'
print(items.count('Java'))
# print(items.index('C++')) # ValueError: 'C++' is not in list

# 排序和反转
items.sort()
print(items)
items.reverse()
print(items)

# 列表生成式
items = [i for i in range(1, 101) if i % 2 == 0]
print(items)

# 嵌套列表
scores = [[70, 80, 90], [65, 75, 85], [77, 88, 99]]
print(scores[0][1])

# 下注双色球
n = int(input('输入下注数：'))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    selected_reds = random.sample(red_balls, 6)
    selected_reds.sort()
    for ball in selected_reds:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    blue_ball = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')