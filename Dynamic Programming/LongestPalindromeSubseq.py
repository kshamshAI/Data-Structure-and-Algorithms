'''Leetcode--------------------------516. Longest Palindromic Subsequence
Solved
Medium
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".'''


class Solution:
    #To find the len of longest palindromic Subsequence
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
            dp[0][i] = 0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i][j-1],dp[i-1][j])  
        return dp[n][n]
       
        
        
    
    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)
        prev = [0 for _ in range(n+1)] 
        for i in range(1,n+1):
            curr = [0 for _ in range(n+1)] 
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = 0 + max(curr[j-1],prev[j])
            prev = curr
        return prev[n]
    

    # To Print the longest palindromic subsequence
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
            dp[0][i] = 0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i][j-1],dp[i-1][j])  
        i ,j= n ,n
        result = []
        while i >0 and j > 0:
            if s[i-1] == s[::-1][j-1]:
                result.append(s[i-1])
                i-=1
                j-=1
            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    j-=1
                else:
                    i-=1 
        result.reverse()
        return "".join(result)  


    
  
s = "mbadm"
s1 =  "leetcode"
print(Solution().longestPalindromeSubseq(s1))

print(Solution().longestPalindromeSubseq1(s1))
            
            

    



        