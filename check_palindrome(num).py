# Check a number given by user a PLINDROME or not

num = int(input("Enter the number to check palindrome: "))

def is_palindrome():
    
    n = num
    result = 0
    while(n>0):
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n // 10
    return (result == num)

print(is_palindrome())
