# _*_coding:utf-8_*_
# __author: a123456
import random

from tools.helper import tool


def partition(arr, l, r):
    """
    以v分割数组， 左边的比v小， 右边的比v大
    :param arr:
    :param l:
    :param r:
    :return:
    """
    p = r
    n = random.randint(l, r)
    tool.swap(l, n, arr)
    v = arr[l]
    i = l + 1

    while 1:
        while i <= r and arr[i] < v:
            i += 1
        while p > l and arr[p] > v:
            p -= 1
        if i > p:
            break
        tool.swap(i, p, arr)
        i += 1
        p -= 1

    tool.swap(l, p, arr)

    return p


def n_largest_ele(arr, l, r, n):
    # 获取第n大的元素
    i = r - n + 1  # 第n大的元素的下标
    # i = n - 1  #
    p = partition(arr, l, r)  # 以p下标分割

    while p != i:
        if p > i:
            # 如果p大于i，选择左边再去获取，舍弃右边
            p = partition(arr, l, p)
        else:
            p = partition(arr, p + 1, r)

    return arr[p]


arr = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36, 99, 98, 95]
for i in [1, 2, 3, 4, 5]:
    arr.sort(reverse=True)
    print(f"第 {i} 大元素是 {arr[i - 1]}, {n_largest_ele(arr, 0, len(arr) - 1, i)}")
