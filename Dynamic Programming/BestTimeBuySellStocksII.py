from typing import List
class Solution:
    def BuyandsellStocks(self,prices:List[int]) ->int:
        n = len(prices)
        def solve(i,transaction):
            if i < 0:
                return 0
            if transaction==1:
                buy = -prices[i] + solve(i-1,0)
                not_buy = 0 + solve(i-1,1)
                max_profit = max(buy,not_buy)
            else:
                sell = prices[i] + solve(i-1,1)
                not_sell = 0 + solve(i-1,0)
                max_profit = max(sell,not_sell)
            return max_profit
        return solve(n-1,1)
    
    # Reecursion O(4**n) space=O(n)
    def BuyandsellStocks1(self,prices:List[int]) ->int:
        n = len(prices)
        def solve(i,transaction):
            if i == n:
                return 0
            if transaction==1:
                buy = -prices[i] + solve(i+1,0)
                not_buy = 0 + solve(i+1,1)
                max_profit = max(buy,not_buy)
            else:
                sell = prices[i] + solve(i+1,1)
                not_sell = 0 + solve(i+1,0)
                max_profit = max(sell,not_sell)
            return max_profit
        return solve(0,1)
    
    # Memoization-O(2*n) space-O(2n)+O(n)
    def BuyandsellStocks2(self,prices:List[int]) ->int:
        n = len(prices)
        dp = [[-1 for _ in range(2)]for _ in range(n)]
        def solve(i,transaction,dp):
            if i == n:
                return 0
            if dp[i][transaction] != -1:
                return dp[i][transaction]
            if transaction==1:
                buy = -prices[i] + solve(i+1,0,dp)
                not_buy = 0 + solve(i+1,1,dp)
                max_profit = max(buy,not_buy)
            else:
                sell = prices[i] + solve(i+1,1,dp)
                not_sell = 0 + solve(i+1,0,dp)
                max_profit = max(sell,not_sell)
            dp[i][transaction]= max_profit
            return dp[i][transaction]
        return solve(0,1,dp)
    
    # Tabulation O(2*n)
    def BuyandsellStocks3(self,prices:List[int]) ->int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n+1)]
        dp[n][0] = 0
        dp[n][1] = 0
        for i in range(n-1,-1,-1):
            for transaction in range(2):
                if transaction==1:
                    buy = -prices[i] + dp[i+1][0]
                    not_buy = 0 + dp[i+1][1]
                    max_profit = max(buy,not_buy)
                else:
                    sell = prices[i] + dp[i+1][1]
                    not_sell = 0 + dp[i+1][0]
                    max_profit = max(sell,not_sell)
                dp[i][transaction]= max_profit
        return dp[0][1]
    
    # Tabulation with space opt O(2*n) space=O(1)
    def BuyandsellStocks4(self,prices:List[int]) ->int:
        n = len(prices)
        prev = [0 for _ in range(2)]
        
        for i in range(n-1,-1,-1):
            curr = [0,0]
            for transaction in range(2):
                if transaction==1:
                    buy = -prices[i] + prev[0]
                    not_buy = 0 + prev[1]
                    max_profit = max(buy,not_buy)
                else:
                    sell = prices[i] + prev[1]
                    not_sell = 0 + prev[0]
                    max_profit = max(sell,not_sell)
                curr[transaction]= max_profit
            prev = curr
            
        return prev[1]
    
prices = [7,1,5,3,6,4]
print(Solution().BuyandsellStocks3(prices))
print(Solution().BuyandsellStocks1(prices))
print(Solution().BuyandsellStocks2(prices))
print(Solution().BuyandsellStocks4(prices))