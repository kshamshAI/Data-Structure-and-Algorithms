'''You are given a string s that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Examples :

Input: s = "ab+"
Output: "+ab"
Explanation: In prefix form, operator comes before operands.
Postfix to Infix: ab+ becomes a + b 
Infix to Prefix: a + b becomes +ab 
Input: s = "ab+c*"
Output: "*+abc"
Explanation:
Postfix to Infix: ab+ becomes (a + b), then with c gives (a + b)*c
Infix to Prefix: (a + b) becomes +ab, then with c gives *+abc
Input: s = "ABC/-AK/L-*"
Output: "*-A/BC-/AKL"
Explanation: 
Postfix to infix: ABC/-AK/L-* becomes (A - (B / C)) * ((A / K) - L)
Convert left part to Prefix: (A - (B / C)) becomes -A/BC
Convert right part to Prefix: ((A / K) - L) becomes -/AKL
Combine both with * to get *-A/BC-/AKL
Constraints:

3 ≤ s.size() ≤ 1.6*104'''


class Solution:
    def postToPre(self, s):
        # Code here
        stack = []
        for char in s:
            if char.isalnum():
                stack.append(char)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                new_exp = char+op1+op2
                stack.append(new_exp)
        return stack[-1]
    
s = "ABC/-AK/L-*"
print(f'Output for Postfix to prefix conversion: {Solution().postToPre(s)}')