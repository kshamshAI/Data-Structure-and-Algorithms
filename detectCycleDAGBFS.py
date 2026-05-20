# Cycle detection in DAG(Directed Acyclic Graph) using BFS (Kahn's Algorithm)
from collections import deque   
    #BFS(Kahn's Algorithm)
class Solution:
    def isCyclic(self, V, edges):
        indegrees = [0 for _ in range(V)]
        result = []
        queue = deque()
        adj_list=[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v]+=1
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)
                
        while(queue):
            node = queue.popleft()
            result.append(node)
            for n in adj_list[node]:
                indegrees[n]-=1
                if indegrees[n] == 0:
                    queue.append(n)
        return (len(result)!=V)