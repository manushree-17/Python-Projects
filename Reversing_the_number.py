def reverse_number(n): 
    rev = 0
    while n > 0: 
        last_digit = n % 10
        rev = rev * 10 + last_digit 
        n = n // 10
    return rev
  
n = int(input("Enter a number: "))
print("Reverse of the given number is", reverse_number(n))