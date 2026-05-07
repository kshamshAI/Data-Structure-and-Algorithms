'''GeeksforGeeks Problem
Minimum number of Coins
Difficulty: Easy Accuracy: 51.25%   Submissions: 115K+Points: 2
Given an infinite supply of each denomination of Indian currency { 1, 2, 5, 10 } and a target value n. Find the minimum number of coins and/or notes needed to make the change for Rs n. 
Examples:
Input: n = 39
Output: 6
Explaination: 39 can be formed using 3 coins of 10 rupees, 1 coin of 5 rupees and 2 coins of 2 rupees so minimum coins required are 6.
Input: n = 121
Output: 13
Explaination: 121 can be formed using 12 coins of 10 rupees and 1 coin of 1 rupees.'''

class Solution:
     def findMin(self, n):
       # code here
        remaining = n
        total = 0
        currency = [1,2,5,10]
        for i in range(len(currency)-1,-1,-1):
            while n >= currency[i]:
                n = n - currency[i]
                total += 1
        return total    
print(Solution().findMin(121))