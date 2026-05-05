'''You are given a string s representing an infix expression. Convert this infix expression to a postfix expression.
Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The precedence order is as follows: (^) has the highest precedence and is evaluated from right to left, (* and /) come next with left to right associativity, and (+ and -) have the lowest precedence with left to right associativity.
Examples :
Input: s = "a*(b+c)/d"
Output: abc+*d/
Explanation: The expression is a*(b+c)/d. First, inside the brackets, b+c becomes bc+. Now the expression looks like a*(bc+)/d. Next, multiply a with (bc+), so it becomes abc+* . Finally, divide this result by d, so it becomes abc+*d/.
Input: s = "a+b*c+d"
Output: abc*+d+
Explanation: The expression a+b*c+d is converted by first doing b*c -> bc*, then adding a -> abc*+, and finally adding d -> abc*+d+.
Input: s = "(a+b)*(c+d)"
Output: ab+cd+*
Explanation: The expression (a+b)*(c+d) is converted by first doing (a+b) -> ab+, then doing (c+d) -> cd+, and finally the expression ab+*cd+ becomes ab+cd+*. 
Constraints:
1 ≤ s.length ≤ 5*103
s[i] can be an operand (a–z, A–Z, 0–9), an operator (+, -, *, /, ^) or a parenthesis ((, ))'''


class Solution:
        #code here
    def set_priority(self,ch):
        if ch == "+" or ch ==  "-":
            return 1
        if ch == "*" or ch ==  "/":
            return 2
        if ch == "^":
            return 3
        
        return 0
        
    def infixtoPostfix(self,s) :      
        stack = []
        result = []
        for char in s:
            # for operands
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                result.append(char)
            # for opening bracket
            elif char == '(':
                stack.append(char)
            # for closing bracket
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())   
                stack.pop() 
            # for operators
            else:
                while stack and (stack[-1] != '(') and ((self.set_priority(stack[-1]) > self.set_priority(char)) or (self.set_priority(stack[-1]) == self.set_priority(char)) and (char != '^')):
                     result.append(stack.pop())
                stack.append(char) 

        while stack:
            result.append(stack.pop())
        return "".join(result)
        
s = 'a*(b+c)/d'     
print(f'infix to postfix output for s: {Solution().infixtoPostfix(s)}')  