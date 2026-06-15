'''Leetcode-----------------------242. Valid Anagram-----------------------------------
Solved
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.'''
class Solution:
    #Brute Force
    def anagram1(self,s:str,t:str) ->bool: #TC=O(2nlogn) as m=n for valid anagram
        m = len(s)
        n = len(t)
     
        if m != n:
            return False
        s1 = sorted(s)  #O(mlogm)
        s2 = sorted(t)  # O(nlogn)
        if s1==s2:
            return True
        return False

    #optimal
    def anagram2(self,s:str,t:str) ->bool:  # TC=O(n) SC=O(26)~O(1)
        m = len(s)
        n = len(t)
        result={}
        if m != n:
            return False
        for i in range(m):
            result[s[i]] = result.get(s[i],0)+1 #O(n)
        for ch in t:  #O(n)
            if ch  not in result:
                return False
            else:
                if result[ch] == 0:
                    return False
                result[ch] = result.get(s[i])-1
        return True
                