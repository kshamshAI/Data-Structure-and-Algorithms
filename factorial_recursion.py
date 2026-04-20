def func(n):
    if n==1:
        return 1
    return(n*func(n-1))
z = int(input("enter number for factorial: "))
x = func(z)
print("The factorial is: ", x)