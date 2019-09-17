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

    _not_result = ["left", "right"]  # search返回，不需要的字段

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
        return {k: node[k] for k in node if k not in self._not_result}

    def _update_node(self, value, node):
        """把新节点拿过来，更新数据"""
        _node = {
            "value": value,
            "num": 1,
            "rank": 1,
            "left": {},
            "right": {},
        }
        node.update(_node)
        self.count += 1

    def search(self, value):
        if not self.root:
            return None

        cur_node = self.root
        while cur_node:
            cur_value = cur_node["value"]

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
            cur_node["rank"] += 1
            cur_value = cur_node["value"]

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                cur_node = cur_node["right"]
            else:
                cur_node = cur_node["left"]
                sub_value = cur_node.get("value", None)
                if sub_value is None or cur_value != sub_value:
                    break

        self._update_node(value, cur_node)

    def _get_min(self, node, use=0):
        if node["left"]:
            if use == 1:
                node["rank"] -= 1

            return self._get_min(node["left"])

        return node

    def get_min(self):
        node = self._get_min(self.root)
        return node

    def _get_max(self, node, use=0):
        if node["right"]:
            if use == 1:
                node["rank"] -= 1

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
                # 如果当前值小于要查询的值， rank加上当前节点左孩子的rank加1
                rank += cur_node["left"].get("rank", 0) + 1
                cur_node = cur_node["right"]
            else:
                cur_node = cur_node["left"]
                sub_value = cur_node.get("value", None)
                if sub_value is None or cur_value != sub_value:
                    rank += cur_node.get("rank", 0)
                    return rank

        return None

    def select(self):
        """查看排名第几的是什么元素"""
        pass

    def ceil(self):
        pass

    def floor(self):
        pass

    @classmethod
    def show(cls):
        r = cls()
        arr = tool.build_test_list(5, 0, 100)
        arr.append(0)
        arr.append(0)
        arr.append(0)
        arr.append(0)
        arr.append(0)
        arr.append(50)
        arr.append(50)
        arr.append(50)
        t = time()
        for i in arr:
            r.insert(i)
        print(time() - t)

        # print(50 in r)
        # print(r.search(0))
        # r.pre_order(r.root)
        # print()
        r.in_order(r.root)
        print()
        t = time()
        print("rank", r.rank(0))
        print((time() - t) * 1000)
        # r.post_order(r.root)
        # print()
        # r.level_order(r.root)
        # print()



bst = BinarySearchTree

if __name__ == '__main__':
    bst.show()
