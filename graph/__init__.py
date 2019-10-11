# _*_coding:utf-8_*_
# __author: a123456
from graph.dense import DenseGraph
from graph.sparse import SparseGraph


class Graph:
    graph_map = {
        1: DenseGraph,
        2: SparseGraph,
    }

    @classmethod
    def new(cls, data, directed, _type=1):
        """
        获取新的图对象
        :param directed:
        :param data:  [[点数量, _], [点, 点]]
        :param _type:
        :return:
        """
        n = data[0][0]
        obj = cls.graph_map[_type](n, directed)
        for v, w in data[1:]:
            obj.add_edge(v, w)

        obj.count_dfs()
        return obj

    @classmethod
    def test(cls):
        """
        0: [0, 8, 7, 6, 5, 4, 3, 2, 1]
        :return:
        """
        t = {
            0: [5, 1, 2, 6, ],
            1: [],
            2: [],
            3: [],
            4: [3, ],
            5: [4, 3],
            6: [4, ],
            7: [9, ],
            8: [],
            9: [12, 10, 11],
            10: [],
            11: [12, ],
            12: [],
            13: [],
        }

        data = [[k, j] for k in t for j in t[k]]
        data.insert(0, [14, 0])

        obj1 = cls.new(data, True)
        obj2 = cls.new(data, True, 2)

        ret1 = obj1.dfs(7)  # 邻接矩阵找到第一个点为最小值
        ret2 = obj2.dfs(7)
        is_connected1 = obj1.is_connected(7, 12)
        is_connected2 = obj2.is_connected(7, 12)
        print(1)


if __name__ == '__main__':
    Graph.test()
