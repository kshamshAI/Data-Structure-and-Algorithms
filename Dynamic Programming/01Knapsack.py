'''-----------------------------------------0 - 1 Knapsack Problem---------------------------------------------------------------
Difficulty: Medium
Given two arrays, val[] and wt[], where each element represents the value and weight of an item respectively, and an integer W representing the maximum capacity of the knapsack (the total weight it can hold).
The task is to put the items into the knapsack such that the total value obtained is maximum without exceeding the capacity W.
Note: You can either include an item completely or exclude it entirely — fractional selection of items is not allowed. Each item is available only once.
Examples :
Input: W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
Output: 3
Explanation: Choose the last item, which weighs 1 unit and has a value of 3.
Input: W = 3, val[] = [1, 2, 3], wt[] = [4, 5, 6] 
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Input: W = 5, val[] = [10, 40, 30, 50], wt[] = [5, 4, 2, 3] 
Output: 80
Explanation: Choose the third item (value 30, weight 2) and the last item (value 50, weight 3) for a total value of 80.'''

class Solution:
    # Recursion
    def knapsack(self, W, val, wt):
        # code here
        def solve(index,weight):
            if index==0:
                if wt[index]<=weight:
                    return val[index]
                return 0
            
            pick = float('-inf') if wt[index]>weight else val[index] + solve(index-1,weight-wt[index])
            unpick = solve(index-1,weight)
            return max(pick,unpick)
        return solve(len(val)-1,W)
    
    # Memoization
    def knapsack(self, W, val, wt):
        # code here
        n = len(val)
        dp = [[-1 for _ in range(W+1)] for _ in range(n)]
        def solve(index,weight,dp):
            if index == 0:
                if wt[index]<=weight:
                    return val[index]
                return 0
            if dp[index][weight] != -1:
                return dp[index][weight]
            if wt[index] > weight:
                pick = float('-inf')
            else:
                pick =  val[index] + solve(index-1,weight-wt[index],dp)
            unpick = 0 + solve(index-1,weight,dp)
            dp[index][weight] = max(pick,unpick)
            return dp[index][weight]
        return solve(n-1,W,dp)
    
    #Tabulation
    def knapsack(self, W, val, wt):
         # code here
        n = len(val)
        dp = [[0 for _ in range(W+1)] for _ in range(n)]
        for w in range(W+1):
          if wt[0] <= w:
                dp[0][w] = val[0]
        for index in range(1,n):
             for weight in range(W+1):
                 pick = float('-inf') if wt[index]>weight else val[index] + dp[index-1][weight-wt[index]]
                 unpick = dp[index-1][weight]
                 dp[index][weight] = max(pick,unpick)
            
        return dp[n-1][W]
    # Tabulation
    def knapsack(self, W, val, wt):
         # code here
        n = len(val)
        prev = [0 for _ in range(W+1)]
        for w in range(W+1):
             if wt[0] <= w:
                 prev[w] = val[0]
        for index in range(1,n):
            curr = [0 for _ in range(W+1)]
            for weight in range(W+1):
                 pick = float('-inf') if wt[index]>weight else val[index] + prev[weight-wt[index]]
                 unpick = prev[weight]
                 curr[weight] = max(pick,unpick)
            prev = curr
        return prev[W]
    
    
    
            
            
