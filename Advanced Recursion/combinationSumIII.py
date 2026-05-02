'''Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9'''
class Solution:
    def backtrack(self,index,total,subset,arr,k,n,result):
        if len(subset) == k and total == n: 
            result.append(subset.copy())
            return
        if total > n:
            return
        if index >= len(arr):
            return
        
        subset.append(arr[index])
        sum = total + arr[index]
        self.backtrack(index+1,sum,subset,arr,k,n,result)
        e = subset.pop()
        sum  -= e
        self.backtrack(index+1,sum,subset,arr,k,n,result)
        return result

    def combinationSum3(self, k: int, n: int) -> list:
        result = []
        arr = [i for i in range(1,10)]
        return self.backtrack(0,0,[],arr,k,n,result)