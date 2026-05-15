# GeeksforGeeks Problem
from collections import deque
class Solution:
    def isCycle(self, V, edges):
        # code here
        visited = [0]*V
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
       
        for i in range(V):
            if visited[i] == 1:
                continue
            queue = deque()
            queue.append((i,-1))
            visited[i] = 1
            while queue:
                node,parent = queue.popleft()
                for n in adj[node]:
                    if visited[n] == 0:
                        visited[n] = 1
                        queue.append((n,node))
                    else:
                        if n != parent:
                            return True
        return False

    def dfs(self,adj,node,parent,visited,V):
        visited[node] = 1
        for n in adj[node]:
            if visited[n] == 0:
                result = self.dfs(adj,n,node,visited,V)
                if result == True:
                    return True
        
            elif visited[n] == 1 and  n != parent:
                return True
                
        return False   
                
        
    def isCycle2(self, V, edges):
        # DFS
        visited = [0]*V
        adj = [[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(V):
            if visited[i] == 1:
                continue
            if self.dfs(adj,i,-1,visited,V) == True:
                return True
        return False
V1 = 4
edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]
V2 = 4
edges2 = [[0, 1], [1, 2], [2, 3]]
print(f'Output1: {Solution().isCycle2(V1,edges1)}, Output2: {Solution().isCycle2(V2,edges2)}')