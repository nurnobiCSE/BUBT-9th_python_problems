# Python program to print all Prime numbers in an Interval
start ,end= 2 ,50
for item in range(start,end+1):
    if item>1:
        for i in range(2,item):
            if(item%i)==0:
                break
        else:
            print(item)