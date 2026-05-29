'''Leetcode Problem------1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
Solved
Medium
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.'''

# Using Floyd-Warshall Algorithm(TC= O(N**3)+O(N**2)+O(E))
import sys
from typing import List
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
       
        dist = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for i in range(n):
            dist[i][i] = 0
            
        for via in range(n):
            for i in range(n):
                for j in range(n):
                  if dist[i][via] != sys.maxsize and dist[via][j] != sys.maxsize:
                        dist[i][j] = min(dist[i][j],dist[i][via]+dist[via][j])
        min_neighbours = n
        city = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count+=1
            if count <= min_neighbours:
                min_neighbours = count
                city = i
        return city
    
# Using Dijkstra's  Algorithm(Time Complexity=O(N(ElogN))
    def findTheCity1(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        
        # Creating Adjency List
        for u, v, w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
           
        pqueue = []
        min_neighbours = n
        city = -1
        
        #Applying dijkstra's on every single node within a loop
        for src in range(n):
            dist = [sys.maxsize for _ in range(n)]
            heapq.heappush(pqueue,[0,src])
            dist[src] = 0
            while pqueue:
                dis,node = heapq.heappop(pqueue)
                for adjNode,weight in adj[node]:
                    new_dis = dis + weight
                    if new_dis < dist[adjNode]:
                        dist[adjNode] = new_dis
                        heapq.heappush(pqueue,[new_dis,adjNode])
            count = 0
            for i in range(n):
                if dist[i] <= distanceThreshold:
                    count+=1
            if count <= min_neighbours:
                min_neighbours = count
                city = src
        return city
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(Solution().findTheCity1(n,edges,distanceThreshold))