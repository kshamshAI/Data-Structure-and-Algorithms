'''Leetcode-------------------------1312. Minimum Insertion Steps to Make a String Palindrome
Solved
Hard
Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.
Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".'''

class Solution:
    
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]
        



    def minInsertions1(self, s: str) -> int:
        n = len(s)
        prev = [0 for _ in range(n+1)] 
        
        for i in range(1,n+1):
            curr =  [0 for _ in range(n+1)] 
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = 0 + max(prev[j],curr[j-1])
            prev = curr
        return n-prev[n]
        


