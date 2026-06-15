'''Leetcode---------------------------------205. Isomorphic Strings
Solved
Easy
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:
Input: s = "f11", t = "b23"
Output: false
Explanation:
The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.
Example 3:
Input: s = "paper", t = "title"
Output: true'''

class Solution:
    def isomorphicStr(self,str1:str,str2:str) ->bool:
        m = len(str1)
        n = len(str2)
        hash_map12 = {}
        hash_map21 = {}
        for i in range(m):
            if str1[i] in hash_map12:
                if hash_map12[str1[i]] != str2[i]:
                    return False    
            else:
                hash_map12[str1[i]] = str2[i] 
        for i in range(m):
            if str2[i] in hash_map21:
                if hash_map21[str2[i]] != str1[i]:
                    return False
            else:
                hash_map21[str2[i]] = str1[i] 
        return True
        

str1='badc'
str2 = 'baba'
   
str3 = 'paperpe'
str4 = 'titlesl'   
print(Solution().isomorphicStr(str1,str2))
print(Solution().isomorphicStr(str3,str4))
