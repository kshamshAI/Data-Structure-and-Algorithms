'''Shortest Path in Undirected Graph
Difficulty: Medium
You are given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each element edges[i] = [u, v] represents an undirected edge between vertices u and v.
Your task is to find the shortest path distance from a given source vertex src to all other vertices in the graph.
If a vertex is not reachable from the source, return -1 for that vertex.
Note: All edges have unit weight (1).
Examples :
Input: V = 9, E = 10, 
edges[][] = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]], src = 0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
Input: V = 4, E = 2,
edges[][]= [[0, 3], [1, 3]], src = 3
Output: [1, 1, -1, 0]
Shortest Path in Undirected Graph
Difficulty: MediumAccuracy: 49.98%Submissions: 187K+Points: 4Average Time: 20m
You are given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each element edges[i] = [u, v] represents an undirected edge between vertices u and v.
Your task is to find the shortest path distance from a given source vertex src to all other vertices in the graph.
If a vertex is not reachable from the source, return -1 for that vertex.
Note: All edges have unit weight (1).
Examples :
Input: V = 9, E = 10, 
edges[][] = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]], src = 0
Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]
Input: V = 4, E = 2,
edges[][]= [[0, 3], [1, 3]], src = 3
Output: [1, 1, -1, 0]'''

from collections import deque
class Solution:
        
    def shortestPath(self, V, edges, src):
        # code here
        
        adj_list = [[] for _ in range(V)]
        distance = [-1]*V
        queue = deque()
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        queue.append((src,0))
        distance[src] = 0
        while queue:
            node,dis = queue.popleft()
            
           
         
            for adjNode in adj_list[node]:
                if distance[adjNode] == -1:
                    distance[adjNode] = dis+1
                    queue.append((adjNode,dis+1))
            
        return distance
V = 9
E = 10, 
edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0
print(Solution().shortestPath(V,edges,src))