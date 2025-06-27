"""
函数
"""
import functools
import random
import time

# 装饰器 - 参数是被装饰的函数  返回值是一个带有装饰功能的函数
def record_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}执行时间：{end_time - start_time:.2f}秒')
        return result
    return wrapper

@record_time
def download(filename):
    """
    下载文件
    """
    print(f'开始下载{filename}.')
    time.sleep(random.random()*10)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    """
    上传文件
    """
    print(f'开始上传{filename}.')
    time.sleep(random.random()*10)
    print(f'{filename}上传成功.')

# 使用@装饰器函数 语法糖
# download = record_time(download)
# upload = record_time(upload)

# 调用装饰后的函数会记录执行时间
download('111.avi')
upload('222.avi')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('111.avi')
upload.__wrapped__('222.avi')

# 递归调用 - @functools.lru_cache():缓存该函数的执行结果从而避免在递归调用的过程中产生大量的重复运算
@functools.lru_cache()
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

print(fac(6))