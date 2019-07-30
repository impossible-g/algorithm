# _*_coding:utf-8_*_
# __author: a123456
from tools import run_time, tool


@run_time
def select_sort(arr: []) -> []:
    """
        选择排序:
            遍历列表，找到列表当前位置到最后位置的最小数，把这个最小数和当前值互换
        :return: []
    """
    assert arr, "not arr"
    length = len(arr)

    for i in range(length):
        min_index = i  # 最小下标

        for j in range(i, length):
            # [i:length] 找到最小数的下标
            if arr[min_index] > arr[j]:
                min_index = j

        # 位置互换
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    array = tool.build_test_list(30, 0, 1000)
    print(array)
    arr0 = sorted(array)

    arr1 = select_sort(array)
    print(arr1 == arr0)
    print(arr1)
