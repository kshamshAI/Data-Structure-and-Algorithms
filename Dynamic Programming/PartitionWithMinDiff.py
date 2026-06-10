'''Minimum sum partition
Difficulty: Hard
Given an array arr[]  containing non-negative integers, the task is to divide it into two sets set1 and set2 such that the absolute difference between their sums is minimum and find the minimum difference.
Examples:
Input: arr[] = [1, 6, 11, 5]
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
Hence, minimum difference is 1.  
Input: arr[] = [1, 4]
Output: 3
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4
Hence, minimum difference is 3.
Input: arr[] = [1]
Output: 1
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {}, sum of Subset2 = 0
Hence, minimum difference is 1.'''

class Solution:
	def minDifference1(self, arr):
		# code here
		n = len(arr)
		total = sum(arr)
		dp = [[False for _ in range(total+1)]for _ in range(n)]
		for index in range(n):
			dp[index][0] = True
		if arr[0] <= total:
			dp[0][arr[0]] = True
		for index in range(1,n):
			for total in range(total+1):
				pick = False if arr[index]>total else dp[index-1][total-arr[index]]
				unpick = dp[index-1][total]
				dp[index][total] = pick or unpick
		min_diff = float('inf')
		for s1 in range(total+1):
			if dp[n-1][s1] ==  True:
				s2 = total -s1
				min_diff = min(min_diff,abs(s1-s2))
		return min_diff

	def minDifference2(self, arr):
			n = len(arr)
			total = sum(arr)
			prev = [False]*(total+1)
			prev[0] = True
			if arr[0] <= total:
				prev[arr[0]] = True
			for index in range(1,n):
				curr = [False]*(total+1)
				for total in range(total+1):
					pick = False if arr[index]>total else prev[total-arr[index]]
					unpick = prev[total]
					curr[total] = pick or unpick
				prev = curr.copy()
			min_diff = float('inf')
			for s1 in range(0,total+1):
				if prev[s1] ==  True:
					s2 = total - s1
					min_diff = min(min_diff,abs(s1-s2))
			return min_diff
		
			
		