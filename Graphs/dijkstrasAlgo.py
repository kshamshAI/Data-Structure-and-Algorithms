'''Dijkstra Algorithm
Difficulty: Medium
Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.
Note: The Graph is connected and doesn't contain any negative weight edge.
It is guaranteed that all the shortest distance will fit in a 32-bit integer.
Examples:
Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
Output: [4, 3, 0]
Explanation:
Shortest Paths:
For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
For 2 to 1 minimum distance will be 3. By following path 2 -> 1
For 2 to 2 minimum distance will be 0. By following path 2 -> 2
Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
Output: [0, 4, 8, 10, 10]
Explanation:
Shortest Paths: 
For 0 to 1 minimum distance will be 4. By following path 0 -> 1
For 0 to 2 minimum distance will be 8. By following path 0 -> 2
For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3 
For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4'''


import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    #Using priority queue (optimal)TC=O(V+E)
    def dijkstra(self, V, edges, src):
        # code here
        adj = [[] for _ in range(V)]
        distance = [float('inf')]*V
        for u, v, d in edges:
            adj[u].append([d,v])
            adj[v].append([d,u])
            
        priority_queue = []
        heapq.heappush(priority_queue,[0,src])
        distance[src] = 0
        while priority_queue:
            dis,node = heapq.heappop(priority_queue)
            if dis > distance[node] :
                 continue
            for d,adjNode in adj[node]:
                    new_d = d + dis
                    if new_d < distance[adjNode]:
                        distance[adjNode] = new_d
                        heapq.heappush(priority_queue,[new_d,adjNode])
        

        return distance
    

       # Using set(time complexity high in python can raise TLE Error)
       def dijkstra1(self, V, edges, src):
        # code here
        adj = [[] for _ in range(V)]
        distance = [float('inf')]*V
        for u, v, d in edges:
            adj[u].append([d,v])
            adj[v].append([d,u])
        my_set =set()
        my_set.add((0,src))
        distance[src] = 0
        while my_set:
            dis,node = min(my_set)
            my_set.discard((dis,node))
            for d,adjNode in adj[node]:
                new_d = d + dis
                if new_d < distance[adjNode]:
                    if distance[adjNode] != float('inf'):
                   
                        my_set.discard((distance[adjNode],adjNode))
                    distance[adjNode] = new_d
                    my_set.add((new_d,adjNode))
        return distance
    
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(Solution().dijkstra(V,edges,src))