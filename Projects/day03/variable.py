"""
变量命名规范：
1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
2：受保护的变量用单个下划线开头。
3：私有的变量用两个下划线开头。
"""
a = 100
b = 123.45
c = 'hello, word'
d = True
e = '100'
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

print(float(a))  # int类型转为float 100.0
print(int(b))  # float转为int 123
print(int(e, base=2))  # str类型按二进制转为int 4
print(int(d))  # bool类型转int true为1 false为0
print(bool(c))  # str类型转bool 不为空True
print(chr(a))  # int转为str d (d对应的编码为100)
print(ord('d'))  # str转为int 100
