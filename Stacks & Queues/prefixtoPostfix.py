'''You are given a string s that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.
Examples:
Input: s = "+AB"
Output: "AB+"
Explanation: In postfix form, operands come first followed by operator.
Prefix to Infix: +AB becomes A + B
Infix to Postfix: A + B becomes AB+
Input: s = "*+ABC"
Output: AB+C*
Explanation: 
Prefix to Infix: *+ABC becomes (A + B)*C
Infix to Postfix: (A + B)*C becomes AB+C* 
Input: s = "*-A/BC-/AKL"
Output: "ABC/-AK/L-*"
Explanation:
Prefix to infix: *-A/BC-/AKL becomes (A - (B / C)) * ((A / K) - L)
Convert left part to Postfix: (A - (B / C)) becomes ABC/-
Convert right part to Postfix: ((A / K) - L) becomes AK/L-
Combine both with * to get ABC/-AK/L-*
Constraints:
3 ≤ s.size() ≤ 100'''

class Solution:
    def preToPost(self, s):
        # Code here
        stack = []
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i].isalnum():
                stack.append(s[i])
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                
                new_exp = f'{operand1}{operand2}{s[i]}'
                stack.append(new_exp)
        return stack[-1 ]
    
s = "*-A/BC-/AKL"
print(f'Output after prefix to postfix conversion: {Solution().preToPost(s)}')