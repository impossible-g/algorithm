# _*_coding:utf-8_*_
# __author: a123456
class SparseGraph:
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

    def add_edge(self, v, w):
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

    def has_edge(self, v, w) -> bool:
        """
        判断这条边存不存在
        :param v:
        :param w:
        :return:
        """
        assert v in self.g, "无法找到的点"
        assert w in self.g, "无法找到的点"

        return w in self.g[v]

    def _dfs(self, v, result, write_ids):
        for point in self.g[v]:
            if point not in result:
                if write_ids: self._ids[point] = self.count

                result.append(point)
                self._dfs(point, result, write_ids)

    def dfs(self, v, write_ids=False):
        result = self.visited
        self._dfs(v, result, write_ids)
        return result

    def count_dfs(self):
        for point in self.g:
            if point not in self.visited:
                self.count += 1
                self.visited.append(point)
                self._ids[point] = self.count
                self.visited = self.dfs(point, write_ids=True)

    def is_connected(self, v, w):
        return self._ids[v] == self._ids[w]
