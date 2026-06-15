'''Leetcode-------------------------------------796. Rotate String
Solved
Easy
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false'''

class Solution:
    def rotate(self,s:str,goal:str) ->bool:
        n = len(s)
        strs = ''
        i = n-1
        while strs != goal or i>0:
            strs+=s[i]
            i-=1
        if strs == s and strs!=goal:
            return False
        return True
    
    def rotate0(self,s:str,goal:str) ->bool: #O(n**2)
        n = len(s)
        strs = s
        if len(s) != len(goal):
            return False
        for i in range(n):    #O(n)
            if strs == goal:
                return True
            strs = strs[-1] + strs[:-1] #O(n)
        return False
    
    def rotate1(self,s:str,goal:str) ->bool:  #O(2n)~O(n)
        n = len(s)
        strs = s + s #O(n)
        if len(s) != len(goal):
            return False
        if goal in strs: #O(n)
            return True
        return False

