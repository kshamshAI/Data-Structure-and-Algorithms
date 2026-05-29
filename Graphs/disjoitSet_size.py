#Disjoint set is used to check for connected components within a dynamic Graph in constant time complexity.
# It can be done in two ways:  1. Union by rank  2. Union by size
# Steps involved:
# Find the ultimate parent of u as pu and ultimate parent of v as pv 
# Compare the size of pu and pv
# Connect the parent having smaller size to the parent with larger size
class Disjoint_Set2:
    def __init__(self,V):
        self.parent = [i for i in range(V)]
        self.size = [1]*V

    def find_parent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    # Union by rank
    def Union_rank(self,u,v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return
        if  self.size[pu] <  self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        elif  self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
