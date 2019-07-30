# _*_coding:utf-8_*_
# __author: a123456
from tools import run_time, tool


class T:
    @classmethod
    def verify(cls, arr, new_arr):
        print(arr == new_arr)
        # print(new_arr)

    @classmethod
    def swap(cls, i1, i2, arr):
        arr[i1], arr[i2] = arr[i2], arr[i1]

    @classmethod
    @run_time
    def select_sort(cls, arr: []) -> []:
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
            cls.swap(i, min_index, arr)

        return arr

    @classmethod
    @run_time
    def insert_sort(cls, arr: []) -> []:
        """
        插入排序:
            纸牌玩法，如果新牌在老牌中间的大小，则把新牌放入中间
        :param arr:
        :return: []
        """
        length = len(arr)

        for i in range(1, length):

            for j in range(i, 0, -1):
                # [1:i:-1] 倒叙遍历，如果前一个数比当前数小，则换位
                if arr[j] < arr[j - 1]:
                    cls.swap(j, j - 1, arr)
                else:
                    break

        return arr

    @classmethod
    @run_time
    def insert_sort_optimize(cls, arr: []) -> []:
        """
        插入排序优化: 对于基本上有序的数据，有很大优势
        :param arr:
        :return:
        """
        length = len(arr)

        for i in range(1, length):

            temp = arr[i]
            j = i  # 当前元素存放位置
            while j > 0 and arr[j - 1] > temp:
                # 倒叙遍历如果碰到比当前元素大的，使比当前元素大的元素向后移一位
                arr[j] = arr[j - 1]
                j -= 1

            # 把当前元素放入应该放入位置
            arr[j] = temp

        return arr

    @classmethod
    @run_time
    def bubble_sort(cls, arr: []) -> []:
        """
        冒泡排序:
            找到最大的，排到最后，n次循环这样的过程，最终排好
        :param arr:
        :return:
        """
        length = len(arr)

        for i in range(length):

            temp_index = 0
            for j in range(0, length - i):
                if arr[j] > arr[temp_index]:
                    temp_index = j
                    # arr[j], arr[j + 1] = arr[j + 1], arr[j]

            cls.swap(length - i - 1, temp_index, arr)

        return arr


sort = T

if __name__ == '__main__':
    array = tool.build_test_list(10000, 0, 100000)
    print(array)

    arr0 = sorted(array)
    sort.verify(arr0, sort.select_sort(array.copy()))
    sort.verify(arr0, sort.insert_sort(array.copy()))
    sort.verify(arr0, sort.insert_sort_optimize(array.copy()))
    sort.verify(arr0, sort.bubble_sort(array.copy()))
