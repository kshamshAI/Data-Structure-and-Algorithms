'''Geeks for Geeks Problem-----------------------Directed Graph Cycle---------------------------------------------------------
Difficulty: Medium
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from vertex u to v.
Examples:
Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
Output: true
Explanation: The diagram clearly shows a cycle 0 → 1 → 2 → 0
Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: false
Explanation: no cycle in the graph
Constraints:
1 ≤ V ≤ 105
0 ≤ E ≤ 105
0 ≤ edges[i][0], edges[i][1] < V'''

class Solution:
    def dfs(self,node,adj_list,visited,path_visited):
        visited[node] = 1
        path_visited[node] = 1
        for n in adj_list[node]:
            if visited[n] == 0 :
                ans = self.dfs(n,adj_list,visited,path_visited)
                if ans ==True:
                    return True
                
            elif path_visited[n] == 1:
                return True
        path_visited[node] = 0
        return False



    def topoSort(self, V, edges):
        # Code here
        visited = [0]*V
        path_visited = [0]*V
        adj_list=[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            
        for i in range(V):
            if visited[i] == 0:
                ans = self.dfs(i,adj_list,visited,path_visited)
                if ans == True:
                    return True
        return False
    

V1 = 4
edges1 = [[0, 1], [1, 2], [2, 0], [2, 3]]
V2 = 4
edges2 = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(f'Output1: {Solution().topoSort(V1,edges1)}')
print(f'Output2: {Solution().topoSort(V2,edges2)}')