# Write program to generate all possible subsequences of an array using recursion:--------------

def subsequences_recursion(arr): 
    result=[] 
    def backtrack(index:int,subset:list):
        n = len(arr)
        if index >= n:
            result.append(subset.copy())
            return 
        #Pick in subset
        subset.append(arr[index])    
        backtrack(index+1,subset)
        #Unpick in subset
        subset.pop()
        backtrack(index+1,subset)

    backtrack(0,[])
    return result
    
    


nums = [1,5,7,9]
print(subsequences_recursion(nums))