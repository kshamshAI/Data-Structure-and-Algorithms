
arr = [5, 9, 8, 3, 6, 7, 1, 4, 2]
left = 0
right = len(arr)-1
while(left<right):
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right -= 1

print(arr)