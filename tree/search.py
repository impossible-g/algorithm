# _*_coding:utf-8_*_
# __author: a123456
from tools import tool, sort


class S:
    @classmethod
    def binary_search(cls, arr: [], e):
        left = 0  # 左边界
        right = len(arr) - 1  # 右边界

        while left <= right:
            m = left + right >> 1  # 找寻一个中间值

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

    for j in range(100):
        li = tool.build_test_list(16, 0, 100)
        n = 5
        li = sort.merge_sort_bu(li)

        i = search.binary_search(li, li[n])
        if n != i:
            print(i, n)
            print(li)