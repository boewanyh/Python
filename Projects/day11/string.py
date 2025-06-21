"""
字符串
"""
s1 = 'hello, world!'
s2 = '''hello
world!
'''
print(s1)
print(s2)

# 转义字符 \n, \t, \', \", \r
s1 = '\'hello\n\tworld!\''
print(s1)
s2 = '\141\x61\u5b9b' # aa宛 八进制 十六进制 Unicode
print(s2)
# 原始字符串 r, R
s3 = r'\'hello\n\tworld!\''
print(s3) # \'hello\n\tworld!\'

# 拼接
s1 = 'hello' + ',' + 'world'
print(s1)
s2 = '!' * 3
print(s2)
s1 += s2
print(s1)

# 比较 - 比较编码大小
s1 = 'A'
s2 = 'a'
print(ord(s1))
print(ord(s2))
print(s1 > s2)

# 成员
print('ll' in 'hello world')
print('ll' not in 'hello world')

# 长度
print(len('hello'))

# 索引和切片
s1 = 'hello, world!'
print(s1[0])
print(s1[0:5])
print(s1[0:5:2])
print(s1[:-1])

# 遍历
s1 = 'hello'
for i in range(len(s1)):
    print(s1[i])

for elem in s1:
    print(elem)

# 方法
s1 = 'hello, world!'
print(s1.capitalize()) # 首字母转大写
print(s1.title()) # 每个单词首字母大写
print(s1.upper()) # 转大写
print('HELLO'.lower()) # 转小写
print(s1) # 原字符串不变

print(s1.find('o')) # 4 查找
print(s1.rfind('o')) # 8 反向查找
print(s1.find('o', 9)) # -1
print(s1.index('o')) # 4
print(s1.rindex('o')) # 8
# print(s1.index('or', 9)) # ValueError: substring not found

print(s1.startswith('he')) # 以。。开头
print(s1.endswith('!')) # 以。。结尾

s2 = 'abc123456'
print(s2.isdigit())  # False 完全由数字构成
print(s2.isalpha())  # False 完全由字母构成
print(s2.isalnum())  # True 是不是由字母和数字构成

print(s1.center(20, '*')) # 居中
print(s1.ljust(20, '*')) # 左对齐
print(s1.rjust(20, '*')) # 右对齐
print('33'.zfill(5)) # 00033
print('-33'.zfill(5)) # -0033 字符串的左侧补零

# 裁剪
s1 = '   -hello, world!-  '
print(s1.strip())
s2 = '-hello, world!-'
print(s2.lstrip('-'))
print(s2.rstrip('-'))

# 替换
s1 = 'aabb'
print(s1.replace('a', 'c'))
print(s1.replace('b', 'c', 1)) # 替换1次

# 拆分合并
s = 'I love you'
arr = s.split()
print(arr)
print('-'.join(arr))

# 编码
a = '宛'
print(a.encode('utf-8'))
print(a.encode('gbk'))