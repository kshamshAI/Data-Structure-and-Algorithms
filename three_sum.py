#Leetcode Problem--15
'''Given an integer array x, return all the triplets [x[i], x[j], x[k]] such that i != j, i != k, and j != k, and x[i] + x[j] + x[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: x = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
x[0] + x[1] + x[2] = (-1) + 0 + 1 = 0.
x[1] + x[2] + x[4] = 0 + 1 + (-1) = 0.
x[0] + x[3] + x[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: x = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: x = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
Constraints:
3 <= x.length <= 3000
-105 <= x[i] <= 105'''

#Optimal --TC-O(NlogN + N**2), SC=O(N)
def three_sum(nums):
    x = nums
    x.sort()
    result = []
    n = len(nums)
    for i in range(n):
        if  i != 0 and (x[i] == x[i-1]):
            continue
       
        j = i + 1
        k = n-1
        while (j < k):
            sum = x[i] + x[j] + x[k]
            if sum < 0:
                j+=1
            elif sum > 0:
                k-=1
            else:
                result.append([x[i],x[j],x[k]])
                j+=1
                k-=1
                # for duplicacy
                while (j<k) and x[j] == x[j-1]:
                    j+=1
                while (j<k) and x[k] == x[k+1]:
                    k-=1

    return result
    
arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))