# GeeksforGeeks Practice================================
class Solution:	
	# Recursion
	def perfectSum(self, arr, target):
		n = len(arr)
		def solve(index,total,dp):
			if index ==  0:
				if total == 0 and arr[0]==0:
					return 2
				if total == 0 or arr[0] == total:
					return 1
				return 0
			pick = 0 if arr[index]>total else solve(index-1,total-arr[index],dp)
			unpick = solve(index-1,total,dp)
			return pick+unpick
			
	
	# Memoization
	def perfectSum1(self, arr, target):
		# code here
		n = len(arr)
		dp = [[-1 for _ in range(target+1)] for _ in range(n)]
		def solve(index,total,dp):
			if index ==  0:
				if total == 0 and arr[0]==0:
					return 2
				if total == 0 or arr[0] == total:
					return 1
				return 0
			if dp[index][total] != -1:
				return dp[index][total]
			pick = 0 if arr[index]>total else solve(index-1,total-arr[index],dp)
			unpick = solve(index-1,total,dp)
			dp[index][total] = pick+unpick
			return dp[index][total]
		
		return solve(n-1,target,dp)
	
	#Tabulation
	def perfectSum2(self, arr, target):
 		# code here
		n = len(arr)
		dp = [[0 for _ in range(target+1)] for _ in range(n)]
		if arr[0] == 0:
			dp[0][0] = 2
		else:
			dp[0][0] = 1
			if arr[0] <= target:
				dp[0][arr[0]] = 1
		for index in range(1,n):
		   for total in range(target+1):
			pick = 0 if arr[index]>total else dp[index-1][total-arr[index]]
			unpick = dp[index-1][total]
			dp[index][total] = pick+unpick
		return  dp[n-1][target]
		
	# Tabulation wuth space opt
	def perfectSum3(self, arr, target):
		# code here
		n = len(arr)
		prev = [0]*(target+1)
		if arr[0] == 0:
			prev[0]=2
		else:
			prev[0] = 1
			if arr[0] <= target:
				prev[arr[0]] = 1		   
		for index in range(1,n):
			curr = [0] *(target+1)
			for total in range(target+1):
				pick = 0 if arr[index]>total else prev[total-arr[index]]
				unpick = prev[total]
				curr[total] = pick + unpick
			prev = curr.copy()
		return prev[target]