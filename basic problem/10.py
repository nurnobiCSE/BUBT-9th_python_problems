#fibonacci serise:
def fibo(n):
    if n<=0:
        print("Incorrect input!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n = int(input("Enter number for fibonacci : "))
num = n
n = fibo(n)
print(f"fibonacci value of {num} is : {n}")
