#  Python Program for factorial of a number
ranges = int(input("input range for factorial : "))
fact = 1

for i in range(1,ranges+1):
    fact = fact*i

print(f"the factorial value of {ranges} is : {fact}")