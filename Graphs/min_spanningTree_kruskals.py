'''Minimum Spanning Tree----------------------------Using Kruskal's Algorithm(Disjoint Set)--------------------------------
Difficulty: MediumAccuracy: 47.82%Submissions: 203K+Points: 4Average Time: 25m
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w.
Input: V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
Output: 4
Explanation:
The Spanning Tree resulting in a weight
of 4 is shown above.
Input: V = 2, E = 1, Edges = [[0 1 5]]
Output: 5 
Explanation: Only one Spanning Tree is possible which has a weight of 5.
Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
The graph is connected and doesn't contain self-loops & multiple edges.'''

#-----------------------------------Solution(Time Complexity=O(ElogE) + O(E*4*alpha))
class Disjoint_Set:
    def __init__(self,V):
        self.parent = [i for i in range(V)]
        self.rank = [1]*V
    
    def find_parent(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
        
    def Union(self,u,v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)
        
        if pu == pv:
            return False
            
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu]+=1
        return True
        
class Solution:
    def spanningTree(self, V, edges):
        new_edges = []
        for u,v,w in edges:
            new_edges.append([w,u,v])
        new_edges.sort()   #O(ElogE)
        ds = Disjoint_Set(V)
        mst_weight = 0
        for w, u, v in new_edges:     #O(E*4*alpha)
            if ds.Union(u,v):
                mst_weight+=w
        return mst_weight