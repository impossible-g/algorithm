# _*_coding:utf-8_*_
# __author: a123456
import math

from tools import tool


class BaseMaxHeap:
    """
        最大堆：数组表示
            一种完全二叉树，子节点总是比父节点小，无序
            父节点下标：i // 2
            子节点下标：left -> 2*i   right -> 2*i+1
    """

    def __init__(self):
        self.heap = [0]

    def __len__(self):
        return len(self.heap) - 1

    def _get_right_child(self, index):
        return self._get_left_child(index) + 1

    def _get_left_child(self, index):
        return index * 2

    def _get_parent(self, index):
        return index // 2

    def _shift_up(self, k):
        """
        比较大的数据上浮
            查看父节点是否大于当前节点，如果大交换位置，同时再次检查
        :param k:
        :return:
        """
        parent = self._get_parent(k)
        while k > 1 and self.heap[parent] < self.heap[k]:
            tool.swap(parent, k, self.heap)
            parent = self._get_parent(k)

    def _shift_down(self, k=1):
        """
        比较小的数据下沉
            从子节点找到最大的数据，使其和父节点交换位置，重复这个操作到，最后元素
        :param k:
        :return:
        """
        while self._get_left_child(k) <= len(self):
            j = self._get_left_child(k)  # 默认使用左节点交换位置
            if j + 1 <= len(self) and self.heap[j + 1] > self.heap[j]:
                # 如果有右节点并且右节点的值大于左节点的值，使用右节点交换
                j += 1

            if self.heap[k] >= self.heap[j]:
                break

            tool.swap(k, j, self.heap)
            k = j

    def insert(self, ele):
        # 插入数据同时维护最大堆
        self.heap.append(ele)
        self._shift_up(len(self))

    def pop(self):
        # 弹出最大元素，同时交换最后一个元素和最大元素在维护最大堆
        tool.swap(len(self), 1, self.heap)
        result = self.heap.pop()

        self._shift_down()
        return result


class MaxHeap(BaseMaxHeap):
    def __init__(self, arr):
        super(MaxHeap, self).__init__()

        for i in arr:
            self.insert(i)


class MaxHeap2(BaseMaxHeap):
    """
    第一个有子节点的下标：len(self) // 2
    """

    def __init__(self, arr: []):
        super(MaxHeap2, self).__init__()

        self.heap.extend(arr)
        i = len(self) // 2
        while i >= 1:
            self._shift_down(i)
            i -= 1


if __name__ == '__main__':
    li = tool.build_test_list(15, 0, 100)
    print(li)
    max_heap = MaxHeap2(li)
    # max_heap = MaxHeap(li)
    print(max_heap.heap)
    while len(max_heap) > 0:
        print(max_heap.pop(), end="\t")
