# Sum of cube of first n natural numbers
n = int(input("Enter n'th number  : "))
sum=0
for i in range(n+1):
    sqr = i**3
    sum = sum+sqr
    i+=1
    print(sum)