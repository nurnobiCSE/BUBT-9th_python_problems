#Python Program for How to check if a given number is Fibonacci number?
import math

def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

def isFibonacci(n):
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n = int(input("check any integer :"))

if (isFibonacci(n) == True):
	print(n, "is a Fibonacci Number")
else:
	print(n, "is a not Fibonacci Number ")
