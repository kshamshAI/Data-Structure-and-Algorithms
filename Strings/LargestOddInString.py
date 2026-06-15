'''Leetcode--------------------------------------1903. Largest Odd Number in String
Solved
Easy
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.
Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".'''
class Solution:
    #Approach 1
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 != 0:  
                return num[0:i+1]  
        return ""

    # Approach 2
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        result = ''
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 != 0:
                while i >=0:
                    result = result + num[i]
                    i-=1
                return result[::-1]
                
            else:
                continue
        return ""
    # Approach 3(Recursive)
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        def solve(index):
            if index <0:
                return ''
            if int(num[index]) % 2 == 1:        
                return num[:index+1]
            return solve(index-1)
        return solve(n-1)
