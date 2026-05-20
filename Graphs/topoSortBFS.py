# Topologiacal sort using BFS(KAHN"s ALGORITHM)
from collections import deque
def topoSort(self, V, edges):
        result = []
        queue=deque()
        indegrees = [0 for _ in range(V)]
        adj_list=[[] for _ in range(V)]
        
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v]+=1
            
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)
                
                
        while queue:
            node = queue.popleft()
            result.append(node)
            for n in adj_list[node]:
                indegrees[n]-=1
                if indegrees[n] == 0:
                    queue.append(n)
        return result# Topologiacal sort using BFS(KAHN"s ALGORITHM)
from collections import deque
def topoSort(self, V, edges):
        result = []
        queue=deque()
        indegrees = [0 for _ in range(V)]
        adj_list=[[] for _ in range(V)]
        
        for u,v in edges:
            adj_list[u].append(v)
            indegrees[v]+=1
            
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)
                
                
        while queue:
            node = queue.popleft()
            result.append(node)
            for n in adj_list[node]:
                indegrees[n]-=1
                if indegrees[n] == 0:
                    queue.append(n)
        return result