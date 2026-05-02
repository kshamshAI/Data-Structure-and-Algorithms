# Leetcode Problem-22
# Generate valid posibble subsequences of parantheses for given n:----
#Time Complexity=O(2**n),Space Complexity=O(n)-Stack space 
class Solution:

    def gen_parantheses(self,index,total,character,result):
        if index >= len(character):
            if total == 0:
                result.append("".join(character))
            return
        if total < 0:
            return
        if total > len(character)//2:
            returngit
        character[index] = "("
        self.gen_parantheses(index+1,total+1,character,result)
        character[index] = ")"
        self.gen_parantheses(index+1,total-1,character,result)
        
           
    def check_valid(self,n):
        result = []
        character = [""]*(2*n)
        self.gen_parantheses(0,0,character,result)
        return result
    
print(Solution().check_valid(4))