# Leetcode Problem-155
'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]'''
class MinStack:

    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val,val])
        else:
            mini = min(self.stack[-1][1],val)
            self.stack.append([val,mini])

    def pop(self) -> None:
        if len(self.stack) == 0:
            return 0
        e = self.stack.pop()    

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        else:    
            top = self.stack[-1][0]
            return top

    def getMin(self) -> int:
        mini = self.stack[-1][1]
        return mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()