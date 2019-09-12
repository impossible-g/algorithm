# _*_coding:utf-8_*_
# __author: a123456
class BinarySearchTree:
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

    def update_node(self, value, node):
        """把新节点拿过来，更新数据"""
        _node = {
            "value": value,
            "num": 1,
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
            self.update_node(value, self.root)
            return

        cur_node = self.root
        while cur_node:
            cur_value = cur_node["value"]

            if cur_value > value:
                cur_node = cur_node["left"]
            elif cur_value < value:
                cur_node = cur_node["right"]
            else:
                cur_node["num"] += 1
                return

        self.update_node(value, cur_node)

    @classmethod
    def show(cls):
        r = cls()
        for i in [10, 11, 12, 13, 9, 8, 7, 6, 9]:
            r.insert(i)

        print(10 in r)
        print(r.search(9))


if __name__ == '__main__':
    BinarySearchTree.show()
