"""
函数
"""

import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len=4): # 用`*`设置命名关键字参数,只能通过“参数名=参数值”的方式来传递和接收参数
    """
    生成指定长度验证码
    :param code_len: 验证码长度，默认4位
    :return: 由大小写英文字母和数字构成的随机字符串验证码
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(5):
    print(generate_code(code_len=5))