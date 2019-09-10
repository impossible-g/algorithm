# _*_coding:utf-8_*_
# __author: a123456
import random

from tools import run_time, tool
from tree import MaxHeap, MaxHeap2, MaxHeap3


class T:
    @classmethod
    def verify(cls, arr, new_arr):
        if arr != new_arr:
            print(new_arr)
            print(arr == new_arr)
        # print(new_arr)

    # ------------------------ n^2 ------------------
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
            tool.swap(i, min_index, arr)

        return arr

    @classmethod
    @run_time
    def insert_sort(cls, arr: [], l=None, r=None, use=0) -> []:
        """
        插入排序:
            纸牌玩法，如果新牌在老牌中间的大小，则把新牌放入中间
        :param arr:
        :param l:
        :param r:
        :param use: 1: 不打印时间
        :return: []
        """
        if l and r:
            length = r - l + 1
            _range = range(l, length)
        else:
            length = len(arr)
            _range = range(1, length)

        for i in _range:

            temp = arr[i]
            j = i  # 当前元素存放位置
            while j > 0 and arr[j - 1] > temp:
                # 倒叙遍历如果碰到比当前元素大的，使比当前元素大的元素向后移一位
                arr[j] = arr[j - 1]
                j -= 1  # 已经交换，但是还没有和前面的当前偏移量的值比较，所以-偏移量

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

            max_index = 0
            for j in range(0, length - i):
                if arr[j] > arr[max_index]:
                    max_index = j
                    # arr[j], arr[j + 1] = arr[j + 1], arr[j]

            tool.swap(length - i - 1, max_index, arr)

        return arr

    # --------------------- n(logn) ---------------------
    @classmethod
    def __merge(cls, arr, l, mid, r):
        new_arr = arr[l: r + 1]  # [l:r+1] 的合并的辅助数组

        i = l  # 左边数组下标开始位
        j = mid + 1  # 右边数组下标开始位
        for k in range(l, r + 1):
            if i > mid:
                # 如果左边数组超出边界，则合并右边数组
                arr[k] = new_arr[j - l]
                j += 1
            elif j > r:
                # 如果右边数组超出边界，则合并左边数组
                arr[k] = new_arr[i - l]
                i += 1
            elif new_arr[i - l] < new_arr[j - l]:
                # 如果左边数组第一个元素小于右边数组第一个元素，则第一个元素位左边数组第一个元素，左边数组下标位加1
                arr[k] = new_arr[i - l]
                i += 1
            else:
                # 反之
                arr[k] = new_arr[j - l]
                j += 1

    @classmethod
    def __merger_sort(cls, arr, l, r):
        if l >= r:
            return

        # if r - l <= 15:
        #     cls.insert_sort(arr, l, r, use=1)
        #     return

        mid = l + r >> 1
        cls.__merger_sort(arr, l, mid)
        cls.__merger_sort(arr, mid + 1, r)
        if arr[mid] > arr[mid + 1]:
            cls.__merge(arr, l, mid, r)

    @classmethod
    @run_time
    def merge_sort_ub(cls, arr: []) -> []:
        """
        归并排序：自上而下的归并
            两两拆分，最后排序
        :param arr:
        :return:
        """
        length = len(arr)
        cls.__merger_sort(arr, 0, length - 1)
        return arr

    @classmethod
    @run_time
    def merge_sort_bu(cls, arr: []) -> []:
        """
        归并排序：自下而上的归并
            两两拆分，最后排序
        :param arr:
        :return:
        """
        length = len(arr)
        sz = 1

        while sz <= length:
            for i in range(0, length - sz, 2 * sz):
                if arr[i + sz - 1] > arr[i + sz]:
                    # 对 [i:i+sz-1] 和 [i+sz: i+2*sz-1] 进行归并排序
                    cls.__merge(arr, i, i + sz - 1, min(i + 2 * sz - 1, length - 1))

            sz += sz

        return arr

    @classmethod
    def __partition(cls, arr, l, r):
        """
        使当前[l:r]区间的数组，以第一个数v分割，左边比v小，右边比v大
        :param arr:
        :param l:
        :param r:
        :return: 分割数组的中间下标
        """
        # p = l  # 分割数组的下标
        # tool.swap(random.randint(l, r), l, arr)  # 避免数组基本上是有序的
        # v = arr[l]
        #
        # for i in range(l + 1, r + 1):
        #     if arr[i] < v:
        #         # 如果p下标之后的元素比分割数组的元素v小，则把当前元素和p下标所在位置交换
        #         p += 1
        #         tool.swap(i, p, arr)
        #
        # tool.swap(l, p, arr)
        # return p
        # ============= 处理数组里有大量重复元素
        p = r  # 分割数组的下标
        tool.swap(random.randint(l, r), l, arr)  # 避免数组基本上是有序的
        v = arr[l]
        i = l + 1
        while 1:
            while i <= r and arr[i] < v: i += 1  # 从左边开始，如果当前元素小于中间元素，位置不变，左值加一
            while p > l and arr[p] > v: p -= 1  # 从右边开始，如果当前元素大于中间元素，位置不变，右值减一
            if i > p: break  # 左边和右边已经分开
            tool.swap(i, p, arr)  # 大值放在右边，小值放在左边，无序的
            i += 1  # 完成一次，左值加一，右值减一
            p -= 1

        tool.swap(l, p, arr)  #
        return p

    @classmethod
    def __quick_sort(cls, arr, l, r):
        """
        :param arr:
        :param l:
        :param r:
        :return:
        """
        if l >= r:
            return

        p = cls.__partition(arr, l, r)
        cls.__quick_sort(arr, l, p - 1)
        cls.__quick_sort(arr, p + 1, r)

    @classmethod
    @run_time
    def quick_sort(cls, arr: []) -> []:
        """
        快速排序：
            每次分割数组，取一个中间值，使得左边比中间值小，右边比中间值大，递归作用
        :param arr:
        :return:
        """
        cls.__quick_sort(arr, 0, len(arr) - 1)
        return arr

    @classmethod
    def __partition3_ways(cls, arr, l, r):
        tool.swap(random.randint(l, r), l, arr)  # 避免数组基本上是有序的
        v = arr[l]

        lt = l  # [l:lt] < v
        gt = r + 1  # [gt: r] > v
        i = l + 1  # 处理过的下标
        while i < gt:
            if arr[i] < v:
                # 如果当前位小于v，把当前位和第二个元素交换
                tool.swap(i, lt + 1, arr)
                i += 1
                lt += 1
            elif arr[i] > v:
                # 如果当前位大于v，把当前位和最后一个元素交换
                tool.swap(i, gt - 1, arr)
                gt -= 1
            else:
                i += 1

        tool.swap(l, lt, arr)  # 把第一个位置的元素与最后一个小于v的元素交换
        return lt, gt

    @classmethod
    def __quick_sort3_ways(cls, arr, l, r):
        if l >= r:
            return

        lt, gt = cls.__partition3_ways(arr, l, r)
        cls.__quick_sort3_ways(arr, l, lt - 1)
        cls.__quick_sort3_ways(arr, gt, r)

    @classmethod
    @run_time
    def quick_sort3_ways(cls, arr: []) -> []:
        """
        快速排序：
            三路排序算法，[l: lt] > v, [lt: gt] = v, [gt: r] < v
        :param arr:
        :return:
        """
        cls.__quick_sort3_ways(arr, 0, len(arr) - 1)
        return arr

    @classmethod
    @run_time
    def shell_sort(cls, arr: []) -> []:
        """
        希尔排序：
            使用偏移量，每次比较几个子序列，用插入排序把数据排好
        :param arr:
        :return:
        """
        offset = len(arr)

        while offset > 1:
            offset = offset // 2

            for i in range(offset, len(arr)):
                # 插入排序
                j = i - offset
                while j >= 0 and arr[j] > arr[j + offset]:
                    tool.swap(j, j + offset, arr)
                    j -= offset

        return arr

    @classmethod
    @run_time
    def heap_sort1(cls, arr):
        max_heap = MaxHeap(arr)
        for i in range(len(arr))[::-1]:
            arr[i] = max_heap.pop()

        return arr

    @classmethod
    @run_time
    def heap_sort2(cls, arr):
        max_heap = MaxHeap2(arr)
        for i in range(len(arr))[::-1]:
            arr[i] = max_heap.pop()

        return arr

    @classmethod
    @run_time
    def heap_sort3(cls, arr):
        max_heap = MaxHeap3(arr)
        return max_heap.heap

    # ===================== time_sort python 内置排序
    @classmethod
    @run_time
    def time_sort(cls, arr: []) -> []:
        """python自带排序：TimeSort"""
        arr.sort()
        return arr


sort = T

if __name__ == '__main__':
    array = tool.build_test_list(5000, 0, 1000000)
    # array.sort()
    arr0 = sort.time_sort(array.copy())

    # ============= n^2
    sort.verify(arr0, sort.select_sort(array.copy()))
    sort.verify(arr0, sort.insert_sort(array.copy()))
    sort.verify(arr0, sort.bubble_sort(array.copy()))
    # ============= nlogn
    sort.verify(arr0, sort.merge_sort_ub(array.copy()))
    sort.verify(arr0, sort.merge_sort_bu(array.copy()))
    sort.verify(arr0, sort.quick_sort(array.copy()))
    sort.verify(arr0, sort.quick_sort3_ways(array.copy()))
    sort.verify(arr0, sort.shell_sort(array.copy()))
    sort.verify(arr0, sort.heap_sort1(array.copy()))
    sort.verify(arr0, sort.heap_sort2(array.copy()))
    sort.verify(arr0, sort.heap_sort3(array.copy()))
