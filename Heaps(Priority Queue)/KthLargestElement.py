'''Geek's Training
Difficulty: Medium
Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Given a 2D matrix mat[][], where mat[i][0], mat[i][1], and mat[i][2] represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .

Example:
Input: mat[][]= [[1, 2, 5],
               [3, 1, 1], 
               [3, 3, 3]]
Output: 11
Explanation: Geek will learn a new move and earn 5 point then on second day he will do running and earn 3 point and on third day he will do fighting and earn 3 points so, maximum merit point will be 11.
Input: mat[][]= [[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]]
Output: 6
Explanation: Geek can perform any activity each day while adhering to the constraints, in order to maximize his total merit points as 6.
Input: mat[][]= [[4, 2, 6]]
Output: 6
Explanation: Geek will learn a new move to make his merit points as 6.
Constraint:
1 ≤ n ≤ 105   
1 ≤  arr[i][j] ≤ 100'''


from typing import List
class Solution:
    # recursion(Time Complexity= m**n) m=number of task,n= number of days,Space Complexity=O(m*n)-stack space
    def solve(self,day,prev,arr):
       
        if day == 0:
            max_point = 0
            for i in range(0,len(arr[0])):
                if i != prev:
                    max_point = max(max_point,arr[day][i])
            return max_point

        for i in range(0,len(arr[0])):
            max_point = 0
            if i != prev:
                max_point = max(max_point,arr[day][i]+ self.solve(day-1,prev,arr))
        return max_point
    def geektraining(self,arr:List[List[int]]) ->int:
        return self.solve(len(arr)-1,len(arr[0]))
    
    # Memoization(tc = O(m*n))
    def solve2(self,day,prev,arr,dp):
       
        if day == 0:
            max_point = 0
            for i in range(0,len(arr[0])):
                if i != prev:
                    max_point = max(max_point,arr[day][i])
            return max_point
        
        if dp[day][prev] != -1:
            return dp[day][prev]

        for i in range(0,len(arr[0])):
            max_point = 0
            if i != prev:
                max_point = max(max_point,arr[day][i]+ self.solve2(day-1,i,arr,dp))
            dp[day][prev] = max_point
        return dp[day][prev]
    
    def geektraining2(self,arr:List[List[int]]) ->int:
        dp = [[-1]*len(arr[0]) for _ in range(len(arr))]
        return self.solve2(len(arr)-1,len(arr[0]),dp)
    
    # tabulation
    def geektraining3(self,mat):
        #code here
        dp = [[-1]*(len(mat[0])+1) for _ in range(len(mat))]
        dp[0][0] = max(mat[0][1],mat[0][2])
        dp[0][1] = max(mat[0][0],mat[0][2])
        dp[0][2] = max(mat[0][0],mat[0][1])
        dp[0][3] = max(mat[0][0],mat[0][1],mat[0][2])
        
        
        for days in range(1,len(mat)):
            for prevTask in range(len(mat[0])+1):
                max_points = 0
                for i in range(len(mat[0])):
                    if i != prevTask:
                        max_points = max(max_points, mat[days][i] + dp[days-1][i])
                        dp[days][prevTask] = max_points
        return dp[len(mat)-1][3]
    
    # tabulation with space opt
    def geektraining3(self,mat):
        prev=[-1]*4
        
        prev[0] = max(mat[0][1],mat[0][2])
        prev[1] = max(mat[0][0],mat[0][2])
        prev[2] = max(mat[0][1],mat[0][0])
        prev[3] = max(mat[0][0],mat[0][1],mat[0][2])
        
        for days in range(1,len(mat)):
            curr = [0]*4
            for prevTask in range(0,4):
                max_points = 0
                for i in range(0,len(mat[0])):
                    if i != prevTask:
                        max_points = max(max_points,mat[days][i] + prev[i])
                    curr[prevTask] = max_points
            prev = curr.copy()
        return prev[3]





    
mat    =[[1, 2, 5],
        [3, 1, 1], 
        [3, 3, 3]]
print(Solution().geektraining3(mat))
        

