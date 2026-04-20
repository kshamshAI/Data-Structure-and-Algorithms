def check_palindrome(str, left, right):
    
    n = len(str)
    left = 0
    right = n-1
    while(left<right):
      if(str[left] != str[right]):
        return False
      left+=1
      right-=1
    return True 
str = input("Enter your string to check palindrome: ")
x = check_palindrome(str, 0, len(str)-1)
print(x)


        
             
    
  
   