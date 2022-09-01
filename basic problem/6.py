#Check Armstrong number :
num = int(input("enter any integer for check : "))
size = len(str(num))
sum =0
temp = num
while temp>0:
    single_digit = temp % 10
    sum += single_digit**size
    temp //=10
if sum==num:
    print(f"{num} is a armstrong number")
else:
    print("not it!")