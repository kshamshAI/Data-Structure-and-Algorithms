#Leetcode Problem-20(Easy)
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
Example 5:
Input: s = "([)]"
Output: false
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''
class Solution:
    def valid_parentheses(self,s:str) ->bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else: 
                if len(stack ) == 0:
                    return False
                if ch == ')' or ch == ']' or ch == '}':
                    e = stack.pop()
                    if (e == '(' and ch == ')') or (e == '[' and ch==']') or (e == '{' and ch == '}'):
                        continue
                    else:
                        return False
        return len(stack) == 0
s1 = "([])"
s2 = "([)]"
print(f'Output for s1:{Solution().valid_parentheses(s1)}, Output for s2:{Solution().valid_parentheses(s2)}')