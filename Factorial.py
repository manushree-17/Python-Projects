def factorial(n): 
   
  return 1 if (n==1 or n==0) else n * factorial(n - 1);  
    
num = int(input("Enter a number: ")) 
   
if num < 0: 
   print("Sorry, factorial does not exist for negative numbers!") 
elif num == 0: 
   print("The factorial of 0 is 1") 
else: 
   print("The factorial of",num,"is",factorial(num))