
#Write a python program to print the frequency of elements in m in list n:................ 
#constraints: 1.  0<elements in n <=10    2. n can have 10**8 elements             3. m can have 10**8 elements

n = [1,2,5,7,9,1,5,3,9,1,5,1,10]

m = [10,111,7,9,1,37,5,2]


def hashing_list(m,n):
    hash_list = [0] * 11
    
    for nums in n:
        hash_list[nums] = hash_list[nums] + 1
        
    for num in m :
        if (num <= 0) or (num >10):
            print(0)
        else:
            print(hash_list[num])

# hashing_list(m,n)


#Write a python program to print the frequency of elements in m in list n:................ 
#constraints: (1) elements in n can be any integer.  (2) n can have 10**8 elements.         (3) m can have 10**8 elements.

def frequency_map(m,n):
    frequency_dict = {}
    for nums in n:     
            frequency_dict[nums] = frequency_dict.get(nums,0) + 1
    for nums in m :
        if nums in n:
            print(frequency_dict[nums])

# frequency_map(m,n)


a = 'abhfdgjffdssaadfgggjuytabs'
b = 'abcfstn'
# Character Hashing
#Write a python program to print the frequency of characters in m in list n:................ 
#constraints: (1) elements in n can be any character of english alphabet in lowercase.  (2) n can have 10**8 chars.         (3) m can have 10**8 chars.

def char_hashing(a,b):
    hash_list = [0] * 25
    for char in a:
        idx1 = ord(char) - 97
        hash_list[idx1] = hash_list[idx1] + 1
    for char in b:
        idx2 = ord(char) - 97
        if hash_list[idx2] not in hash_list:
           print(0)
        else:
            print(hash_list[idx2])  
print(char_hashing(a,b))      