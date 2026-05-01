# Write a function to print factors of a number inside a list................

num = int(input('Enter the number to print its factors: '))
factors = []
n = num
# Brute Force Approach
def Factors1():
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

# Better Approach
def Factors2():
    for i in range(1,int((n/2)+1)):
         if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors

# Optimal Approach
from math import sqrt
def Factors3():
    for i in range(1,int(sqrt(n)+1)):
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n//i)
    return (sorted(factors))


    
print(Factors3())
factors.clear   