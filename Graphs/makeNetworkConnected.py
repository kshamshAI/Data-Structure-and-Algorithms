'''Leetcode Problem-1319---------1319. Number of Operations to Make Network Connected
Solved
Medium
Topics
premium lock icon
Companies
Hint
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.'''

#-------------------------------------------Solution----------------------------------------------------
from typing import List
class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    def find(self,u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self,u,v):
        pu,pv = self.find(u),self.find(v)
        if pu == pv:
            return True
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu]+=1
        return False
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extra_edges = 0
        ds = DisjointSet(n)
        for u,v in connections:
            if ds.union(u,v):
                extra_edges+=1

        count = 0
        for i in range(n):
            if ds.find(i) == i:
                count += 1
        if extra_edges >= count-1:
            return (count - 1)
        return -1
    
    
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(Solution().makeConnected(n,connections))

        