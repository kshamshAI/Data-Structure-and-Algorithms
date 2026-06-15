'''Leetcode--------------188. Best Time to Buy and Sell Stock IV
Solved
Hard
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Constraints:
1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000'''

from typing import List
class Solution:
	# recursion TC=(2**n*3*2), O(n)-stack
	def maxProfit1(self, prices: List[int],k:int) -> int:
		n = len(prices)
		def solve(index,buy,limit):
			if index == 0:
				return 0
			if limit == 0:
				return 0
			if buy ==1:
				buy_ = -prices[index] + solve(index+1,0,limit)
				not_buy = 0 + solve(index+1,1,limit)
				profit = max(buy_,not_buy)
			else:
				sell = prices[index] + solve(index+1,1,limit-1)
				not_sell = 0 + solve(index+1,0,limit)
				profit = max(sell,not_sell)
			return profit
		return solve(0,1,k)
	
	# Memoization O(6n),space = O(6n)+O(n)-stack
	def maxProfit1(self, prices: List[int],k:int) -> int:
		n = len(prices)
		dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
		def solve(index,buy,limit,dp):
			if index == 0:
				return 0
			if limit == 0:
				return 0
			if dp[index][buy][limit] !=0:
				return dp[index][buy][limit] 
			if buy ==1:
				buy_ = -prices[index] + solve(index+1,0,limit,dp)
				not_buy = 0 + solve(index+1,1,limit,dp)
				profit = max(buy_,not_buy)
			else:
				sell = prices[index] + solve(index+1,1,limit-1,dp)
				not_sell = 0 + solve(index+1,0,limit,dp)
				profit = max(sell,not_sell)
			dp[index][buy][limit] = profit
			return dp[index][buy][limit] 
		return solve(0,1,k,dp)
	

	# Tabulation  tc=O(6n) space=O(6n)
	def maxProfit1(self, prices: List[int],k:int) -> int:
		n = len(prices)
		dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
		for index in range(n-1,-1,-1):
			for buy in range(2):
				for limit in range(1,k+1):
					if limit == 0:
						profit = 0
					elif buy ==1:
						buy_ = -prices[index] + dp[index+1][0][limit]
						not_buy = 0 + dp[index+1][1][limit]
						profit = max(buy_,not_buy)
					else:
						sell = prices[index] + dp[index+1][1][limit-1]
						not_sell = 0 + dp[index+1][0][limit]
						profit = max(sell,not_sell,dp)
					dp[index][buy][limit] = profit
			return dp[0][1][k]


	# Tabulation with space opt tc = O(6n) space=O(6)~O(1)
	def maxProfit4(self, prices: List[int],k:int) -> int:
		n = len(prices)
		next_ = [[0 for _ in range(k+1)] for _ in range(2)]
		
		for index in range(n-1,-1,-1):
			curr = [[0 for _ in range(k+1)] for _ in range(2)]
			for buy in range(2):
				for limit in range(1,k+1): 
					if limit == 0:
						profit = 0
					elif buy == 1:
						buy_ = -prices[index] + next_[0][limit]
						not_buy = next_[1][limit]
						profit = max(buy_,not_buy)
					else:
						sell = prices[index] + next_[1][limit-1]
						not_sell = 0 + next_[0][limit]
						profit = max(sell,not_sell)
					curr[buy][limit] = profit
			next_ = curr
		return next_[1][k]
	 