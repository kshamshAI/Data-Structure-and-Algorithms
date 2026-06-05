class MinHeap:
    def __init__(self,val):
        self.arr = []
        self.val = val
        self.count = 0

    
    def heapify_up(self,arr,ind):
        n = len(arr)
        parent_ind = (ind-1)//2
        if ind < n and arr[ind] > arr[parent_ind]:
            arr[ind],arr[parent_ind] = arr[parent_ind],arr[ind]
            self.heapify_up(arr,parent_ind)

    def heapify_down(self,arr,ind):
        n = len(arr)
        largest_ind = ind
        left_child = 2*ind + 1
        right_child = 2*ind + 2
        if left_child < n and arr[largest_ind] < arr[left_child]:
            largest_ind = left_child
        if right_child < n and arr[largest_ind] < arr[right_child]:
            largest_ind = right_child 
        if ind != largest_ind:
            arr[ind],arr[largest_ind] = arr[largest_ind],arr[ind]
            self.heapify_down(arr,largest_ind)

        

    def insert(self,val):
    
        self.arr.append(val)
        self.count+=1
        self.heapify_up(self.arr,self.count)

    def change_val(self,ind,val):
        if self.arr[ind] < val:
            self.arr[ind] = val
            self.heapify_down(self.arr,ind)
            
        else:
            self.arr[ind] = val
            self.heapify_up(self.arr,ind)
           

    def extract_min(self):
        n = len(self.arr)
        temp = self.arr[0]
        if self.count == 0:
            return None
        self.arr[0],self.arr[n-1] = self.arr[n-1],self.arr[0]
        if self.count > 0:
            self.heapify_down(self.arr,0)
        self.arr.pop()
        self.count -= 1
        return temp
    
    def get_min(self): 
        return self.arr[0] if self.count > 0 else None
    
    def get_size(self):
        return self.count
    
    def Isempty(self):
        if self.count == 0:
            return True
        return False
class MaxHeap:
    def __init__(self,val):
        self.arr = []
        self.val = val
        self.count = 0

    def heapify_up(self,arr,ind):
        n = len(arr)
        parent_ind = (ind-1)//2
        if ind < n and arr[ind] > arr[parent_ind]:
            arr[ind],arr[parent_ind] = arr[parent_ind],arr[ind]
            self.heapify_up(arr,parent_ind)

    def heapify_down(self,arr,ind):
        n = len(arr)
        largest_ind = ind
        left_child = 2*ind + 1
        right_child = 2*ind + 2
        if left_child < n and arr[largest_ind] < arr[left_child]:
            largest_ind = left_child
        if right_child < n and arr[largest_ind] < arr[right_child]:
            largest_ind = right_child 
        if ind != largest_ind:
            arr[ind],arr[largest_ind] = arr[largest_ind],arr[ind]
            self.heapify_down(arr,largest_ind)

        

    def insert(self,val):
    
        self.arr.append(val)
        self.count+=1
        self.heapify_up(self.arr,self.count)

    def change_val(self,arr,ind,val):
        if arr[ind] < val:
            arr[ind] = val
            self.heapify_up(arr,ind)
        else:
            arr[ind] = val
            self.heapify_down(arr,ind)

    def extract_max(self):
        n = len(self.arr)
        temp = self.arr[0]
        if self.count == 0:
            return None
        self.arr[0],self.arr[n-1] = self.arr[n-1],self.arr[0]
        if self.count > 0:
            self.heapify_down(self.arr,0)
        self.arr.pop()
        self.count -= 1
        return temp
    
    def get_max(self): 
        return self.arr[0] if self.count > 0 else None
    
    def get_size(self):
        return self.count
    
    def Isempty(self):
        if self.count == 0:
            return True
        return False
