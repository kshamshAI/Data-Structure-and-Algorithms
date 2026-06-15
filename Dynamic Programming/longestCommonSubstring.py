'''GeeksforGeeks-----Given two strings s1 and s2, determine the length of the longest substring that appears in both strings.
Examples:
Input: s1 = "ABCDGH", s2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" with a length of 4.
Input: s1 = "abc", s2 = "acb"
Output: 1
Explanation: The longest common substrings are "a", "b", "c" all having length 1.
Input: s1 = "YZ", s2 = "yz"
Output: 0
Explanation: Comparison is case-sensitive, so 'Y' ≠ 'y' and 'Z' ≠ 'z'. Hence, no common substring exists.'''


class Solution:
    def longCommSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        maxi = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxi = max(maxi,dp[i][j])
        return maxi
    
    def longCommSubstr1(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        prev = [0 for _ in range(n+1)] 
        maxi = 0
        for i in range(1,m+1):
            curr = [0 for _ in range(n+1)] 
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    maxi = max(maxi,curr[j])
            prev = curr
        return maxi
s1 = "ABCDGH"
s2 = "ACDGHR"
print(Solution().longCommSubstr(s1,s2))