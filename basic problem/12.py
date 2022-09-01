# Python Program for n\’th multiple of a number in Fibonacci Series
def fiboSpace(k,n):
    f1=0
    f2=1
    i=2
    while i!=0:
        f3=f1+f2
        f1=f2
        f2=f3
        if f2%k==0:
            return n*i
        i+=1
    return
n=int(input("enter maximum value : "))
k=int(input("enter minimum value : "))
result = fiboSpace(k,n)
print(f"position of n'th multiple of {k} in fibo series : ",result)