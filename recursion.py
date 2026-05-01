# Functional parametric recursion
# Write a function to print 1 to N using recursion both head and tail..................

# Head recursion
def func_head(i=1,N=5):
    if i > N :
        return
    print(i)
    func_head(i+1,N)
# Tail recursion
def func_tail(i=1,N=5):
    if i >= N :
        return
    func_head(i,N)
    print(i)

# Write a function to print N to 1 using recursion both head and tail..................

# Head recursion
def func_head_reverse(N=5):
    if N <= 0 :
        return
    print(N)
    func_head_reverse(N-1)

# Tail recursion
def func_tail_reverse(i=5,N=5):
    if i < 0:
        return
    func_tail_reverse(i-1,N)
    print(i)

func_tail()