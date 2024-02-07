def armstrong(num):
    temp=num
    sum=0
    while temp>0:
        remainder=temp % 10
        sum=sum+remainder**3
        temp=temp//10
    if num==sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

num=int(input("Enter a number: "))
armstrong(num)