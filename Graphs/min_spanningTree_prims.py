'''Minimum Spanning Tree
Difficulty: Medium
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w.
Input: V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
Output: 4
Explanation:
The Spanning Tree resulting in a weight
of 4 is shown above.
Input: V = 2, E = 1, Edges = [[0 1 5]]
Output: 5 
Explanation: Only one Spanning Tree is possible which has a weight of 5.'''

# ----------------------------Solution using Prim's Algorithm(Time Complexity=O(2*(ElogE))~O(ElogE))

import heapq
class Solution:
    def spanningTree(self, V, edges):
        # code here(Prim's Algorithm)
        adj = [[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        Sum = 0
        mst = []
        visited = [0]*V
        pqueue = []
        heapq.heappush(pqueue,(0,0,-1))# (weight,node,parent)
        while pqueue:
            weight,node,parent = heapq.heappop(pqueue)
            if visited[node] == 0:
                visited[node] = 1
                if parent != -1:
                    Sum += weight
                mst.append((parent,node))
                for adjNode,wt in adj[node]:
                    heapq.heappush(pqueue,(wt,adjNode,node))
        return Sum

V = 3
E = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(Solution().spanningTree(V,edges))   