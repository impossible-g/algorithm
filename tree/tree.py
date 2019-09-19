# _*_coding:utf-8_*_
# __author: a123456
import queue
import sys
from time import time

from tools.helper import tool


class Traverse:
    def operate(self, node):
        print(f"{node['value']}", end="\t")

    def pre_order(self, node):
        """
        前序遍历，访问根节点，遍历左节点，遍历右节点
        """
        if node:
            self.operate(node)
            getattr(self, sys._getframe().f_code.co_name)(node["left"])
            getattr(self, sys._getframe().f_code.co_name)(node["right"])

    def in_order(self, node):
        """
        中序遍历，遍历左节点，访问根节点，遍历右节点
        """
        if node:
            getattr(self, sys._getframe().f_code.co_name)(node["left"])
            self.operate(node)
            getattr(self, sys._getframe().f_code.co_name)(node["right"])

    def post_order(self, node):
        """
        后序遍历，遍历左节点，遍历右节点，访问根节点
        """
        if node:
            getattr(self, sys._getframe().f_code.co_name)(node["left"])
            getattr(self, sys._getframe().f_code.co_name)(node["right"])
            self.operate(node)

    def level_order(self, node):
        """
        层序遍历，借助队列实现，按层级结构打印出来
        """
        if not node:
            return -1

        q = queue.Queue()
        q.put(node)

        while not q.empty():
            _node = q.get()

            self.operate(_node)

            if _node.get("left"):
                q.put(_node["left"])

            if _node.get("right"):
                q.put(_node["right"])


class BinarySearchTree(Traverse):
    """二分搜索树"""

    def operate(self, node):
        self.temp_li.append(node["value"])

    def __init__(self):
        self.root = {}
        self.count = 0

    def __contains__(self, value):
        if not self.root:
            return False

        cur_node = self.root
        while cur_node:
            cur_value = cur_node["value"]

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                cur_node = cur_node["right"]
            else:
                return True

        return False

    def _get_result(self, node):
        return node

    def _update_node(self, value, node, **kwargs):
        """把新节点拿过来，更新数据"""
        _node = {
            "value": value,
            "num": 1,  # 重复加1
            "sub_num": 1,  # 子节点数量, 包含自身
            "left": {},
            "right": {},
        }
        node.update(_node)
        node.update(kwargs)
        self.count += 1

    def _insert_node(self, value, node, **kwargs):
        _node = {
            "value": value,
            "num": 1,
            "sub_num": node.get("sub_num", 0) + 1,
            "left": {},
            "right": {},
        }
        if node:
            k = "left" if node["value"] < value else "right"
            _node[k] = node
        _node.update(kwargs)
        self.count += 1
        return _node

    def search(self, value, use=0):
        if not self.root:
            return None

        cur_node = self.root
        while cur_node:
            cur_value = cur_node["value"]
            if use == 1:
                cur_node["sub_num"] -= 1

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                cur_node = cur_node["right"]
            else:
                return self._get_result(cur_node)

        return None

    def insert(self, value):
        """
        插入节点， 如果节点为空，则初始化一个节点，
        不听更换当前节点，直到确定要插入节点，更新它
        :param value:
        :return:
        """
        if not self.root:
            self._update_node(value, self.root)
            return

        cur_node = self.root
        while cur_node:
            cur_node["sub_num"] += 1
            cur_value = cur_node["value"]

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                cur_node = cur_node["right"]
            else:
                p_node = cur_node
                p_node["num"] += 1
                num = p_node["num"]
                cur_node = cur_node["left"]
                sub_value = cur_node.get("value", None)
                if sub_value is None or cur_value != sub_value:
                    # todo 新节点继承老节点所有东西
                    p_node["left"] = self._insert_node(value, cur_node, num=num)
                    return

        self._update_node(value, cur_node)

    def _get_min(self, node, use=0):
        if node["left"]:
            if use == 1:
                node["sub_num"] -= 1

            return self._get_min(node["left"])

        return node

    def get_min(self):
        node = self._get_min(self.root)
        return node

    def _get_max(self, node, use=0):
        if node["right"]:
            if use == 1:
                node["sub_num"] -= 1

            return self._get_max(node["right"])

        return node

    def get_max(self):
        node = self._get_max(self.root)
        return node

    def del_min(self):
        node = self._get_min(self.root, use=1)
        node.clear()
        self.count -= 1

    def del_max(self):
        node = self._get_max(self.root, use=1)
        node.clear()
        self.count -= 1

    def rank(self, value):
        """查找一个元素的排名"""
        if not self.root:
            return None

        rank = 1
        cur_node = self.root
        while cur_node:
            cur_value = cur_node["value"]

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                # 如果当前值小于要查询的值， rank加上当前节点左孩子的sub_num加1
                rank += cur_node["left"].get("sub_num", 0) + 1
                cur_node = cur_node["right"]
            else:
                cur_node = cur_node["left"]
                sub_value = cur_node.get("value", None)
                if sub_value is None or cur_value != sub_value:
                    rank += cur_node.get("sub_num", 0)
                    return rank

        return None

    def select(self, rank):
        """查看排名第几的是什么元素"""
        if not self.root:
            return None

        _rank = 0
        cur_node = self.root
        while cur_node:
            left_sub_num = cur_node["left"].get("sub_num", 0)

            if left_sub_num >= rank - _rank:
                # 如果排名小于左边子节点数量，表示这个排名在左边子节点内
                cur_node = cur_node["left"]
            elif left_sub_num < rank - _rank:
                # 如果当前值小于要查询的值， rank加上当前节点左孩子的sub_num加1
                _rank += cur_node["left"].get("sub_num", 0) + 1
                if _rank == rank:
                    # 如果排名相同，则返回当前节点
                    return cur_node

                cur_node = cur_node["right"]

        return None

    def _floor(self, value, node):
        if not node:
            return node

        if node["value"] > value:
            return self._floor(value, node["left"])
        elif node["value"] < value and node["right"] and (
                node["right"]["value"] <= value or self._get_min(node["right"])["value"] <= value):
            # 如果当前节点小于28，那么当前节点的左子树是不用考虑的，
            # 如果当前节点右子节点小于28，则从右节点继续循环
            return self._floor(value, node["right"])
        else:
            return node

    def floor(self, value):
        return self._floor(value, self.root)

    def _ceil(self, value, node):
        if not node:
            return node

        if node["value"] > value and node["left"] and (
                node["left"]["value"] >= value or self._get_max(node["left"])["value"] >= value):
            # 如果当前节点大于28，那么当前节点的右子树是不用考虑的
            # 如果当前节点的左子节点大于28，则从左子节点继续循环
            return self._ceil(value, node["left"])
        elif node["value"] < value:
            return self._ceil(value, node["right"])
        else:
            return node

    def ceil(self, value):
        return self._ceil(value, self.root)

    def get_floor_and_ceil(self, value):
        return self.floor(value), self.ceil(value)

    def del_ele(self, value):
        """
        删除任意节点，
            使用它左子树的最大节点代替 或者 使用它右子树的最小节点代替
        """
        if value not in self:
            return

        self.count -= 1
        node = self.search(value, use=1)

        if node["left"]:
            _node = self._get_max(node["left"], use=1)
        elif node["right"]:
            _node = self._get_min(node["right"], use=1)
        else:
            node.clear()
            return

        node["value"] = _node["value"]
        _node.clear()
        return

    @classmethod
    def test_rank(cls):
        r = cls()
        num = 88888
        arr = tool.build_test_list(5000, 0, 10000, no_print=True)
        arr.append(num)
        arr.sort()
        for i in arr:
            r.insert(i)

        r1 = arr.index(num) + 1
        r2 = r.rank(num)

        print(r1 == r2, r1, r2)

    @classmethod
    def test_floor(cls):
        r = cls()
        value = 888
        arr = tool.build_test_list(20, 0, 10000, no_print=True)

        for i in arr:
            r.insert(i)
            a = 449 in r

        base_arr = arr.copy()
        arr.sort()
        f1 = 0
        for i in arr:
            if i - value < 0:
                f1 = i
            elif i - value == 0:
                f1 = i
                break

        f2 = r.floor(value).get("value", 0)

        if f1 != f2:
            raise Exception(f1, f2)

    @classmethod
    def test_ceil(cls):
        r = cls()
        value = 888
        arr = tool.build_test_list(500, 0, 10000, no_print=True)

        for i in arr:
            r.insert(i)

        base_arr = arr.copy()
        arr.sort()
        f1 = 0
        for i in arr:
            if i - value > 0:
                f1 = i
                break
            elif i - value == 0:
                f1 = i
                break

        f2 = r.ceil(value).get("value", 0)

        if f1 != f2:
            raise Exception(f1, f2)

    @classmethod
    def test_insert(cls):
        r = cls()
        arr = tool.build_test_list(5000, 0, 100000, no_print=True)
        # arr = [1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
        for i in arr:
            r.insert(i)

        r.temp_li = []
        r.in_order(r.root)
        arr.sort()
        if r.temp_li != arr:
            raise Exception(r.temp_li, arr)


bst = BinarySearchTree

if __name__ == '__main__':
    # [bst.test_rank() for i in range(100)]
    [bst.test_insert() for i in range(100)]
    [bst.test_floor() for i in range(100)]
    for i in range(100):
        print(f"\r{i}", end="")
        bst.test_ceil()
