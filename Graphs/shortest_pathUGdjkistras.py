'''Shortest Path in an Undirected Graph using Dijksta's Algorithm-------------------------------
Difficulty: Medium
You are given a weighted undirected graph with n vertices numbered from 1 to n and m edges along with their weights. Find the shortest path between vertex 1 and vertex n. Each edge is given as {a, b, w}, denoting an edge between vertices a and b with weight w
If a path exists, return a list of integers where the first element is the total weight of the shortest path, and the remaining elements are the nodes along that path (from 1 to n). If no path exists, return a list containing only {-1}.
Note: The driver code will internally verify your returned list.
If both the path and its total weight are valid, only the total weight will be displayed as output.
If your list contains only -1, the output will be -1.
If the returned list is invalid, the output will be -2.
Examples :
Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 
Input: n = 2, m= 1, edges = [[1, 2, 2]]
Output: 2
Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2. 
Input: n = 2, m= 0, edges = [ ]
Output: -1
Explanation: Since there are no edges, so no answer is possible.
Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n+m)'''
#User function Template for python3
from typing import List
import sys
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj = [[] for _ in range(0,n+1)]
        distance = [sys.maxsize for _ in range(0,n+1)]
        parent = [i for i in range(0,n+1)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        priority_queue = []
        heapq.heappush(priority_queue,[0,1])
        distance[1] = 0
        
        while priority_queue:
            dis,node = heapq.heappop(priority_queue)
            if dis > distance[node]:
                continue
        
            for adjNode,weight in adj[node]:
                new_d = dis + weight
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d
                    heapq.heappush(priority_queue,[new_d,adjNode])
                    parent[adjNode] = node
        if distance[n] == sys.maxsize:
            return [-1]
        shortest_path = []
        node =  n
        while parent[node] != node:
            shortest_path.append(node)
            node = parent[node]
        shortest_path.append(1)  #source node
        shortest_path.reverse()
        shortest_path.insert(0,distance[n])
        return shortest_path

n = 5 
m= 6 
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
n1 = 2
m1= 1 
edges1 = [[1, 2, 2]]
print(Solution().shortestPath(n1,m1,edges1))