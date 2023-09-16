class Solution:
    def __init__(self):
        self.n = 1005
        self.father = [i for i in range(self.n)]
    
    def find(self, u):
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u
    
    def same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(len(edges)):
            if self.same(edges[i][0], edges[i][1]):
                return edges[i]
            self.join(edges[i][0], edges[i][1])
        return []
        