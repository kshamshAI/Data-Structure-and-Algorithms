class Solution1:
    def solve(self,height,i):
        if i == 0:
            return 0
        energy1 = self.solve(height,i-1) + abs(height[i] - height[i-1])
        if i > 1:
            energy2 = self.solve(height,i-2) + abs(height[i] - height[i-2])
        else:
            energy2 = float('inf')
        min_energy = min(energy1,energy2)
        return min_energy
        
    def minCost(self, height):
        # code here
        n = len(height)
        return self.solve(height,n-1)
class Solution2:
    def solve(self,height,i,dp):
        if i == 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        energy1 = self.solve(height,i-1,dp)+abs(height[i] - height[i-1])
        if i == 1:
            return energy1
        
        energy2 = self.solve(height,i-2,dp)+abs(height[i] - height[i-2])
        
        dp[i] = min(energy1,energy2)
        return dp[i]
        
    def minCost(self, height):
        # code here
        n = len(height)-1
        dp = [-1] * (n+1)
        return self.solve(height,n,dp)
    

class Solution3:        
    def minCost(self, height):
        # code here
        n = len(height)
        dp = [-1] * (n)
        # return self.solve(height,n,dp)
        dp[0] = 0
        for i in range(1,n):
            energy1 = dp[i-1] + abs(height[i] - height[i-1])
            if i > 1:
                energy2 = dp[i-2] + abs(height[i] - height[i-2])
                
            else:
                energy2 = float('inf')
            dp[i] = min(energy1,energy2)
        return dp[n-1]
    
class Solution4:
       
    def minCost(self, height):
        # code here
        n = len(height)
        prev2 = 0
        prev = 0
        for i in range(1,n):
            energy1 = prev + abs(height[i] - height[i-1])
            if i>1:
                energy2 = prev2 +  abs(height[i] - height[i-2])
            else:
                energy2 = float('inf')
            curr = min(energy1,energy2)
            prev2 = prev
            prev = curr
        return prev

height = [30, 20, 50, 10, 40]
print(Solution1().minCost(height))
print(Solution2().minCost(height))
print(Solution3().minCost(height))
print(Solution4().minCost(height))
