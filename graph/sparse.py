# _*_coding:utf-8_*_
# __author: a123456
class DenseGraph:
    """
    稀疏图：使用邻接表实现
        {
            0: {1, 2},  # set()
            1: {2},
            2: {0},
        }
    """

    def __init__(self, n: int, directed: bool):
        self.n = n  # 有多少点
        self.m = 0  # 有多少条边
        self.__directed = directed  # 是否有向
        self.g = {i: set() for i in range(n)}

    @property
    def directed(self):
        return self.__directed

    def add_edge(self, v: int, w: int):
        """
        添加一条边
        :param v: 点的名称
        :param w: 点的名称
        :return:
        """
        if self.has_edge(v, w):
            return

        self.g[v].add(w)
        if not self.directed:
            self.g[w].add(v)

        self.m += 1

    def has_edge(self, v: int, w: int) -> bool:
        """
        判断这条边存不存在
        :param v:
        :param w:
        :return:
        """
        assert v in self.g, "无法找到的点"
        assert w in self.g, "无法找到的点"

        return w in self.g[v]

    @classmethod
    def test(cls):
        obj = cls(10, False)

        obj.add_edge(9, 9)
        obj.add_edge(9, 8)
        print(1)


if __name__ == '__main__':
    DenseGraph.test()
