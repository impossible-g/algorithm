# _*_coding:utf-8_*_
# __author: a123456


class UF:
    def __init__(self):
        self.parent = []  # 记录每个点的前导是什么
        self.rank = []  # rank[i]表示跟节点为i的的树的高度

    def add(self, e):
        self.parent.append(e)
        self.rank.append(1)

    def find(self, p):
        """查找p这个节点的根节点"""
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # 路径压缩，使这个节点指向父节点的父节点
            p = self.parent[p]

        return p

    def union(self, p, q):
        """连接两个点"""
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.rank[p_root] < self.rank[q_root]:
            # 此时根为q_root，q_root高度比p_root高，所以不需维护rank数组
            self.parent[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    @classmethod
    def test(cls):
        c = cls()

        for i in range(10):
            c.add(i)

        for i in range(8):
            c.union(1, i)

        print(c.parent)
        print(c.is_connected(0, 5))


if __name__ == '__main__':
    UF.test()
