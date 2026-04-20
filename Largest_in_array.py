
def largest_arr(nums):
    n = len(nums)
    largest = nums[0]

    for i in range(0, n):
        largest = max(largest, nums[i])

    return largest

arr = [55, 32, -97, 99, 3, 67]
x = largest_arr(arr)
print(x)

