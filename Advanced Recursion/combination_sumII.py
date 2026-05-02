#LEETCODE PROBLEM-40
#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.
#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
#Example 2:
#Input: candidates = [2,5,2,1,2], target = 5
#Output: [[1,2,2],[5]]
#Constraints:
#1 <= candidates.length <= 100
#1 <= candidates[i] <= 50
#1 <= target <= 30

class Solution:
    def backtrack(self,index,total,subset,candidates,result):
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        if index >= len(candidates):
            return
       
        for i in range(index,len(candidates)):
            if (i > index) and (candidates[i] == candidates[i-1]):
                continue
            subset.append(candidates[i])
            sum = total - candidates[i]
            self.backtrack(i+1,sum,subset,candidates,result)
            subset.pop()
        return result
        
    def combinationSum2(self, candidates:list, target: int) -> list:
        candidates = sorted(candidates)
        result = []
        return self.backtrack(0,target,[],candidates,result)