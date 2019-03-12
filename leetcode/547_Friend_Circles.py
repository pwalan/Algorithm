from _ast import List

# 使用并查集解决

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0

        n = len(M)
        uf = UnionFind(range(n))

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 0:
                    continue
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.count


class UnionFind():
    def __init__(self, alist):
        n = len(alist)
        self.count = 0
        self.parent = [-1] * n
        self.rank = [0] * n
        for i in range(n):
            self.parent[i] = i
            self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] > self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1