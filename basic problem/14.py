  # Sum of squares of first n natural numbers
n = int(input("Enter n'th number  : "))
sum=0
for i in range(n+1):
    sqr = i**2
    sum = sum+sqr
    i+=1
    print(sum)