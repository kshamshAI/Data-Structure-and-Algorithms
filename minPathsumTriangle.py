
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def solve(i,j,triangle):
            if i == len(triangle)-1:
                return triangle[i][j]
            
            down =  triangle[i][j]+solve(i+1,j,triangle)
            dia =  triangle[i][j]+solve(i+1,j+1,triangle)
            return min(down,dia)
        return solve(0,0,triangle)  
    
    
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp =[[-1]*n for _ in range(n)]
        def solve(i,j,triangle,dp):
            if i == len(triangle)-1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            
            down =  triangle[i][j]+solve(i+1,j,triangle,dp)
            dia =  triangle[i][j]+solve(i+1,j+1,triangle,dp)
            dp[i][j]= min(down,dia)
            return dp[i][j]
        return solve(0,0,triangle,dp)   
    
      
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp =[[-1]*n for _ in range(n)]
        for k in range(n):
            dp[n-1][k] = triangle[n-1][k]
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                
                down =  triangle[i][j]+dp[i+1][j]
                dia =  triangle[i][j]+dp[i+1][j+1]
                dp[i][j]= min(down,dia)
           
        return dp[0][0] 
    

    def minimumTotal4(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = [0]*n
        for k in range(n):
            prev[k] = triangle[n-1][k]
        for i in range(n-2,-1,-1):
            curr = [0]*(i+1)
            for j in range(0,i+1):
                
                down =  triangle[i][j]+prev[j]
                dia =  triangle[i][j]+prev[j+1]
                curr[j]= min(down,dia)
                
            prev = curr.copy()
           
        return prev[0] 
           
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal4(triangle))