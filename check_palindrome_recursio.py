def check_palindrome(str, left, right):
    if(left>=right):
        return True
    if(str[left] !=str[right]):
        return False
    return check_palindrome(str, left+1, right-1)

str = input("Enter string to check palindrome: ")
x = check_palindrome(str, 0, len(str)-1)
print(x)
