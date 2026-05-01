#Write a program to calculate two sum array .return index as answer... e.g: [1,4]....Given that
# 1. use element once
# 2. only one solution exists

# Brute force Approach
def two_sum_array(arr,target):
    n = len(arr)
    result = []
    for i in range(0, n-1):
        j = i+1
        while(j<n):
            if (arr[i] + arr[j]) == target:
                result.append(i)
                result.append(j)
            j += 1
    return result
# Time Complexity--O(N**2)


#Optimal Approach
def two_sum_opt(arr,target):
    temp = {}
    for i in range(0,len(arr)):
        remaining = target - arr[i]
        
        if remaining in temp:
            return [temp[remaining],i]
        temp[arr[i]] = i
# Time Complexity--O(N)



# nums = [3,3]
# x = two_sum_opt(nums,6)
# print(x)

def isPalindrome(x: int) -> int:
    result = 0
    num = x if x>0 else -1*x
    while(num>0):
        last_digit = num % 10
        result = result*10 + last_digit
        num = num // 10
    return result if x>0 else -1*result
y = 9646324351
print(isPalindrome(1534236469))
print(y.bit_count())