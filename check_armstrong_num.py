# Check if a number is Armstrong number or not......
# e.g. 153 
# number of digits = 3
# 1**3 + 5**3 + 3**3 = 153

num = int(input("Enter the number to check wether armstrong number or not : "))

def is_armstrong():
    n = num
    total = 0
    num_digit = len(str(n))
    while(n>0):
        last_digit = n % 10
        total =  total + last_digit**num_digit
        n = n // 10
    return (total == num)

print(is_armstrong())

# Time complexity = O(log(N) base 10)
# Space complexity = O(1)