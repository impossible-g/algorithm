# _*_coding:utf-8_*_
# __author: a123456
import math

from tools import sort, tool


class MaxHeap:
    """
    最大堆：数组表示
        一种完全二叉树，子节点总是比父节点小，无序
        父节点下标：i // 2
        子节点下标：left -> 2*i   right -> 2*i+1
    """

    def __init__(self, arr):
        self.heap = [0]

        for i in arr:
            self.insert(i)

    def __len__(self):
        return len(self.heap) - 1

    def __shift_up(self, k):
        """
        比较大的数据上浮
            查看父节点是否大于当前节点，如果大交换位置，同时再次检查
        :param k:
        :return:
        """
        while k > 1 and self.heap[k // 2] < self.heap[k]:
            sort.swap(k // 2, k, self.heap)
            k //= 2

    def __shift_down(self, k=1):
        """
        比较小的数据下沉
            从子节点找到最大的数据，使其和父节点交换位置，重复这个操作到，最后元素
        :param k:
        :return:
        """
        while 2 * k <= len(self):
            j = 2 * k  # 默认使用左节点交换位置
            if j + 1 <= len(self) and self.heap[j + 1] > self.heap[j]:
                # 如果有右节点并且右节点的值大于左节点的值，使用右节点交换
                j += 1

            if self.heap[k] >= self.heap[j]:
                break

            sort.swap(k, j, self.heap)
            k = j

    def insert(self, ele):
        # 插入数据同时维护最大堆
        self.heap.append(ele)
        self.__shift_up(len(self))

    def pop(self):
        # 弹出最大元素，同时交换最后一个元素和最大元素在维护最大堆
        sort.swap(len(self), 1, self.heap)
        result = self.heap.pop()

        self.__shift_down()
        return result


li = tool.build_test_list(15, 0, 100)
max_heap = MaxHeap(li)
print(max_heap.heap)
m = max_heap.pop()
print(m)
print(max_heap.heap)
