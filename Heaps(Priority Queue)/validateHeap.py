class Solution:
    def __init__(self):
        self.arr = []
        self.val = None

    def IsMinHeap(self,arr):
        n = len(arr)
        if len(arr) == 0:
            return None
        # check for internal nodes
        for i in range((n//2)-1,-1,-1):
            left_child = 2*i + 1
            right_child = 2*i + 2
            if left_child < n and arr[i] < arr[left_child]:
                return True
            if right_child < n and arr[i] < arr[right_child]:
                return True
        return False
    
    def IsMaxHeap(self,arr):
        n = len(arr)
        if len(arr) == 0:
            return None
        for i in range((n//2)-1,-1,-1):
            left_child = 2*i + 1
            right_child = 2*i + 2
            if left_child < n and arr[i] > arr[left_child]:
                return True
            if right_child < n and arr[i] > arr[right_child]:
                return True
        return False

        
arr = [4,6,9,12,16,13,19,21]
print(Solution().IsMinHeap(arr))