# Wwrite a function to check wether a given string is palindrome using recursion?..............

s = input("Enter String to check: ") 
l =0
r = len(s)-1

def is_palindrome(string,left,right):
    if string[left] != string[right]:
        return False
    if left <= right:
        is_palindrome(string,left+1,right-1)
        return True

x = is_palindrome(s,l,r)
print(x)