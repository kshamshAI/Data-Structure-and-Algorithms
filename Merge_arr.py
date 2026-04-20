def merge_arr(left, right):
    result = []
    i=0 
    j = 0
    m = len(right)
    n = len(left)
    while(i < n and j < m):
        if(left[i]< right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if(i < n):
        while(i<n):
            result.append(left[i])
            i+=1
    if(j < m):
        while(j<m):
            result.append(right[j])
            j+=1
    return result

# left = [1, 3, 6]
# right = [2, 4, 7, 8]
# x = merge_arr(left, right)
# print(x)