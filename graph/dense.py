# _*_coding:utf-8_*_
# __author: a123456
class DenseGraph:
    """
    稠密图：使用邻接矩阵的实现方式
        [
            [False, False],
            [False, False]
        ]
    """

    def __init__(self, n: int, directed: bool):
        self.n = n  # 有多少点
        self.m = 0  # 有多少条边
        self.__directed = directed  # 是否有向
        self.g = [[False] * n for i in range(n)]

    @property
    def directed(self):
        return self.__directed

    def add_edge(self, v: int, w: int):
        """
        添加一条边
        :param v: 点的下标
        :param w: 点的下标
        :return:
        """
        if self.has_edge(v, w):
            return

        self.g[v][w] = True
        if not self.directed:
            self.g[w][v] = True

        self.m += 1

    def has_edge(self, v: int, w: int) -> bool:
        """
        判断这条边存不存在
        :param v:
        :param w:
        :return:
        """
        assert 0 < v < self.n, "下标越界"
        assert 0 < w < self.n, "下标越界"

        return self.g[v][w]

    @classmethod
    def test(cls):
        obj = cls(10, False)

        obj.add_edge(9, 9)
        obj.add_edge(9, 8)
        print(1)


if __name__ == '__main__':
    DenseGraph.test()
