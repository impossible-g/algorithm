# _*_coding:utf-8_*_
# __author: a123456
from tools.helper import run_time, tool


class S:

    @classmethod
    @run_time
    def index(cls, arr: [], e):
        return arr.index(e)

    @classmethod
    @run_time
    def binary_search(cls, arr: [], e):
        left = 0  # 左边界
        right = len(arr) - 1  # 右边界

        while left <= right:
            # m = left + right >> 1  # 找寻一个中间值
            m = left + (right - left >> 1)

            if arr[m] > e:
                # 如果中间值大于需查找值，则抛弃右区间数据
                right = m - 1
            elif arr[m] < e:
                # 如果中间值小于需查找值，则抛弃左区间数据
                left = m + 1
            else:
                return m


search = S

if __name__ == '__main__':

    li = tool.build_test_list(16000000, 0, 1000000000)
    n = 5
    li = sorted(li)

    i = search.binary_search(li, li[n])
    l1 = search.index(li, li[n])
    if n != i:
        print(i, n)
        print(li)


