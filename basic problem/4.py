# Python Program for simple interest
p = float(input("enter the principle (ammount): "))
t = float(input("enter the time : "))
r = float(input("enter the rate : "))

simple_interest = (p*t*r)/100
#compound_interest = p*((1+r/100)**t-1)
print(f"Simple interest is : {simple_interest:.3f}")