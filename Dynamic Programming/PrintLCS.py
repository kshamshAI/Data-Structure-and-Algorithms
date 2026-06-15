# Printing Longest Common Subsequence between two strings through DP Table:
from typing import List
class Solution:
    def LongestCommonSubsequence(self,s1:str,s2:str) ->List:
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j],dp[i][j-1]) 
        result = []
        i = m
        j = n
        while i>0 and j>0:
            if s1[i-1] == s2[j-1]:
                result.append(s1[i-1])
                i-=1
                j-=1
            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    j-=1
                else:
                    i-=1
        result = result[::-1]
        return "".join(result)
s1 = 'abcde'
s2 = 'bdgek'
print(Solution().LongestCommonSubsequence(s1,s2))


                

