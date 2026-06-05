'''Leetcode-----------703. Kth Largest Element in a Stream

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.
You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.
Implement the KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]
Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8'''
import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.res = nums
        n = len(nums)
        heapq.heapify(self.res)
        while len(self.res)>k:
            heapq.heappop(self.res)

    def add(self, val: int) -> int:
        if len(self.res) < self.k:
            heapq.heappush(self.res,val)
        elif val > self.res[0]:
            heapq.heappop(self.res)
            heapq.heappush(self.res,val)
        
        return self.res[0]

        
        
        
    
k = 4
nums = [7, 7, 7, 7, 8, 3]
add = [2, 10, 9, 9]

obj = KthLargest(k,nums)
for i in range(0,4):
    print(obj.add(add[i]))
