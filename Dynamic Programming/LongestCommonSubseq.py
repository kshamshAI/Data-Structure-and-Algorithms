'''Leetcode-----------------------1143. Longest Common Subsequence-----------------------------------
Solved
Medium
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.'''

class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        def solve(i,j):
            if i < 0 or j < 0:
                return 0
           
            if text1[i] == text2[j]:
                return 1 + solve(i-1,j-1)
            return 0 + max(solve(i-1,j),solve(i,j-1))
        return solve(m-1,n-1)
        
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # m+1xn+1 dp to save the base condition as there is no negative index for tabulation(shifting of index)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        def solve(i,j,dp):
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i-1] == text2[j-1]:
                return 1 + solve(i-1,j-1,dp)
            dp[i][j] = 0 + max(solve(i-1,j,dp),solve(i,j-1,dp))
            return dp[i][j]
        return solve(m,n,dp)
     
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in  range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j]= 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
    
    def longestCommonSubsequence4(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        prev = [-1 for _ in range(n+1)]
        for j in range(n+1):
            prev[0] = 0
        
        for i in range(1,m+1):
            curr = [-1 for _ in range(n+1)]
            curr[0]=0
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    curr[j]= 1 + prev[j-1]
                else:
                    curr[j] = 0 + max(prev[j],curr[j-1])
            prev = curr
        return prev[n]
           
text1 = "abcde"
text2 = "ace"  
print(Solution().longestCommonSubsequence1(text1,text2))  
print(Solution().longestCommonSubsequence2(text1,text2))  
print(Solution().longestCommonSubsequence3(text1,text2))   
print(Solution().longestCommonSubsequence4(text1,text2))          
            
            
        