def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n = int(input("Enter index to get Fibonacci number: "))
x = fibonacci(n)
print(x)