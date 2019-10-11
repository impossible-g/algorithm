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

        self.count = 0  # 联通分量
        self.visited = []  # 遍历所得结果
        self._ids = {}  # 使用并查集的方式判断两点是否相连接

    def clear(self):
        self.count = 0  # 联通分量
        self.visited = []  # 遍历所得结果
        self._ids = {}  # 使用并查集的方式判断两点是否相连接

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
        assert 0 <= v < self.n, "下标越界"
        assert 0 <= w < self.n, "下标越界"

        return self.g[v][w]

    def _dfs(self, v, result, write_ids):
        for i, b in enumerate(self.g[v]):
            if not b:
                continue

            if i not in result:
                if write_ids: self._ids[i] = self.count

                result.append(i)
                self._dfs(i, result, write_ids)

    def dfs(self, v, write_ids=False):
        result = self.visited
        self._dfs(v, result, write_ids)
        return result

    def count_dfs(self):
        for point, _ in enumerate(self.g):
            if point not in self.visited:
                self.count += 1
                self.visited.append(point)
                self._ids[point] = self.count
                self.visited = self.dfs(point, write_ids=True)

    def is_connected(self, v, w):
        return self._ids[v] == self._ids[w]
