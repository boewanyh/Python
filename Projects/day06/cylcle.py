"""
循环结构
"""
# for-in循环
total = 0
for i in range(1,101):
    total += i
print(total)

# while循环
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# break 和 continue
total = 0
i = 1
while True:
    if i % 2 !=0:
        i += 1
        continue # 放弃本次循环进入下一轮
    total += i
    i += 1
    if i > 100:
        break # 终止所在循环
print(total)