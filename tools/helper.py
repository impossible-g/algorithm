# _*_coding:utf-8_*_
# __author: a123456
import random
import time
from functools import wraps


def run_time(func):
    """打印函数运行时间, 毫秒"""

    @wraps(func)  # 获取函数自身名称
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - begin} s")
        return result

    return inner


class T:
    @classmethod
    @run_time
    def build_test_list(cls, n: int, range_l: int = 0, range_r: int = 10) -> []:
        """
        构建测试排序用列表
        :param n:  生成数量
        :param range_l: 左边界
        :param range_r: 右边界
        :return: []
        """
        assert range_l < range_r, "range_l >= range_r"

        arr = [random.randint(range_l, range_r) for i in range(n)]
        return arr

    @classmethod
    @run_time
    def build_order_list(cls, n: int, range_l: int = 0, range_r: int = 10) -> []:
        """
        构建测试排序用列表， 基本有序的列表
        :param n:  生成数量
        :param range_l: 左边界
        :param range_r: 右边界
        :return: []
        """
        assert range_l < range_r, "range_l >= range_r"

        arr = [random.randint(range_l, range_r) for i in range(n)]

        for i in range(10):
            i1 = random.randint(0, n - 1)
            i2 = random.randint(0, n - 1)
            arr[i1], arr[i2] = arr[i2], arr[i1]

        return arr


tool = T

if __name__ == '__main__':
    test_list = tool.build_test_list(10, 0, 10)
