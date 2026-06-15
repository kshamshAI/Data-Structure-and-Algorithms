'''Leetcode---------------------------14. Longest Common Prefix-------------------------
Solved
Easy
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        result =''
        base_word = strs[0]
        for i in range(len(base_word)):
            j = 1
            while j < n:
                if i == len(strs[j]) or base_word[i] != strs[j][i]:
                    return result
                j+=1
            result+=base_word[i]
                      
        return result
          