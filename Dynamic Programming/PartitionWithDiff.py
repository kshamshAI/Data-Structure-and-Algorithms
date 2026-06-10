''' Geeks for Geeks-------------------Partitions with Given Difference
Difficulty: Medium
Given an array arr[] and an integer diff, count the number of ways to partition the array into two subsets such that the difference between their sums is equal to diff.
Note: A partition in the array means dividing an array into two subsets say S1 and S2 such that the union of S1 and S2 is equal to the original array and each element is present in only one of the subsets.
Examples :
Input: arr[] = [5, 2, 6, 4], diff = 3
Output: 1
Explanation: There is only one possible partition of this array. Partition : [6, 4], [5, 2]. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.
Input: arr[] = [1, 1, 1, 1], diff = 0 
Output: 6 
Explanation: We can choose two 1's from indices [0,1], [0,2], [0,3], [1,2], [1,3], [2,3] and put them in sum1 and remaning two 1's in sum2.
Thus there are total 6 ways for partition the array arr. 
Input: arr[] = [3, 2, 7, 1], diff = 4  
Output: 0
Explanation: There is no possible partition of the array that satisfy the given difference. '''
class Solution:
    
        # code here
    def PerfectSum(self,arr,target):
        n = len(arr)
        prev = [0 for _  in range(target+1)]
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= target:
                prev[arr[0]] = 1
        for index in range(1,n):
            curr = [0 for _  in range(target+1)]
            for total in range(target+1):
                pick = 0 if arr[index]>total else prev[total-arr[index]]
                unpick = prev[total]
                curr[total] = pick+unpick
            prev = curr
        return prev[target]
    def countPartitions(self, arr, diff):
        n = len(arr)
        total = sum(arr)
        if (total-diff)<0  or (total-diff) % 2 == 1:
            return 0
        target = (total-diff)//2
        count = self.PerfectSum(arr,target)
        return count
        