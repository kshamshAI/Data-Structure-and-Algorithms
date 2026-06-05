class Solution:
    
    # implement max heap
    def heapifyMax(self,arr,n,ind):
        
        largest = ind
        left_child = 2*ind + 1
        right_child = 2*ind + 2
        if left_child < n and arr[largest] < arr[left_child]:
            largest = left_child
        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child
        if ind  != largest:
            arr[ind],arr[largest] = arr[largest],arr[ind]
            self.heapifyMax(arr,n,largest)

    def heapifyMin(self,arr,n,ind):
        
        largest = ind
        left_child = 2*ind + 1
        right_child = 2*ind + 2
        if left_child < n and arr[largest] > arr[left_child]:
            largest = left_child
        if right_child < n and arr[largest] > arr[right_child]:
            largest = right_child
        if ind  != largest:
            arr[ind],arr[largest] = arr[largest],arr[ind]
            self.heapifyMin(arr,n,largest)
   

    def heapSortasc(self,arr):
        n = len(arr)
        internal_node = (n//2)-1
        for ind in range(internal_node,-1,-1):
            self.heapifyMax(arr,n,ind)

        for last_ind in range(n-1,0,-1):
                arr[0],arr[last_ind] = arr[last_ind],arr[0]
                self.heapifyMax(arr,last_ind,0)
        return arr
    
    def heapSortdsc(self,arr):
        n = len(arr)
        internal_node = (n//2)-1
        for ind in range(internal_node,-1,-1):
            self.heapifyMin(arr,n,ind)

        for last_ind in range(n-1,0,-1):
                arr[0],arr[last_ind] = arr[last_ind],arr[0]
                self.heapifyMin(arr,last_ind,0)
        return arr
    
nums = [3,2,3,1,2,4,5,5,6]
arr = [7,6,4,1,9,9,10,11]
print(Solution().heapSortasc(arr))
print(Solution().heapSortdsc(nums))


                             code