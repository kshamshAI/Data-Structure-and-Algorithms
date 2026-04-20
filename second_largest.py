# BRUTE FORCE APPROACH

def sec_largest(nums):
    largest = float("-inf")
    second_largest = float("-inf")
    n = len(nums)
    for i in range(0, n):
        largest = max(largest, nums[i])
    for i in range(0, n):
        if (nums[i]>second_largest and nums[i] != largest):
            second_largest =  nums[i]
    return second_largest

arr = [55, 32, 97, -55, 45, 32, 88, 21]
x = sec_largest(arr)
print(x)

# TC = O(2N) app.= O(N)
# SC = O(1)