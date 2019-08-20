# _*_coding:utf-8_*_
# __author: a123456
from tools import sort, tool


class MaxHeap:
    """
    最大堆：数组表示
        一种完全二叉树，子节点总是比父节点小，无序
    """

    def __init__(self, arr):
        self.heap = [0]

        for i in arr:
            self.insert(i)

    def __shift_up(self, k):
        while k > 1 and self.heap[k // 2] < self.heap[k]:
            sort.swap(k // 2, k, self.heap)
            k //= 2

    def __shift_down(self, k):
        sort.swap(k, 1, self.heap)

    def insert(self, ele):
        self.heap.append(ele)
        self.__shift_up(len(self.heap) - 1)

    def pop(self):
        result = self.heap[1]
        self.__shift_down(len(self.heap) - 1)
        return result


li = tool.build_test_list(10, 0, 100)
max_heap = MaxHeap(li)
print(1)
