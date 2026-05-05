# GeeksforGeeks Problem-Prefix to Infix Conversion (TC-O(N),SC-O(N)---------
'''You are given a string S of size N that represents the prefix form of a valid mathematical expression. The string S contains only lowercase and uppercase alphabets as operands and the operators are +, -, *, /, %, and ^.Convert it to its infix form.
Example 1:
Input: *-A/BC-/AKL
Output: ((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
Your Task:
Your task is to complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
3<=|S|<=104'''


class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for char in pre_exp[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_exp = f'({operand1}{char}{operand2})'
                stack.append(new_exp)
                
        return stack[-1]
                
s = "*-A/BC-/AKL"
print(f'Output for s after prefix to infix Conversion: {Solution().preToInfix(s)}')