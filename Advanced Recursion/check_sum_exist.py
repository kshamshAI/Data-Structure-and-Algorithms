# Write a progaram to check if there exists subsequences for a target sum in an array or not:-----return bool
#Recursion
def subsequences(nums:list,target:int) ->list:
    n = len(nums)

    def backtrack(index:int,total:int):
        if total == target:
            return True  
        if total > target:
            return False
        elif index >= n:
            return False
        sum = total + nums[index]
        pick = backtrack(index+1,sum)
        if pick:
            return True
        sum = total
        unpick =backtrack(index+1,sum)
        return unpick

    result=backtrack(0,0)
    return result


nums = [1,2,3,4,6,8,4]
target = 6
print(subsequences(nums,target))