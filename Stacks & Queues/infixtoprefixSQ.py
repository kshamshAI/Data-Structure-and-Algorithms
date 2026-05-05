# 1.Reverse the Input
# 2.Do the Post fix conversion
# 3.Reverse the resultant of step 2
class Solution:
    def set_priority(self,ch):
        if ch == '+' or ch == '-':
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == '^':
            return 3
        return 0


    def infixtoPrefix(self,s):
        s = s[::-1]
        stack = []
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and  stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.set_priority(stack[-1]) > self.set_priority(char):
                    result.append(stack.pop())
                stack.append(char)
        while stack:
            result.append(stack.pop())
        return "".join(result[::-1])  
s = "a+b*c+d"
print(f'Output for infix to prefix conversion: {Solution().infixtoPrefix(s)}')