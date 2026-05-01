# Write a progaram to generate all possible subsequences for a target sum from an array:--------------

def subsequences(nums:list,target:int) ->list:
    result = []
    n = len(nums)

    def backtrack(index:int,total:int,subset:list):

        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        elif index >= n:
            return
        subset.append(nums[index])
        sum = total + nums[index]
        backtrack(index+1,sum,subset)
        e = subset.pop()
        sum -= e
        backtrack(index+1,sum,subset)

    backtrack(0,0,[])
    return result


nums = [1,2,3,4,5,6,7,8,9]
target = 9


print(subsequences(nums,target))