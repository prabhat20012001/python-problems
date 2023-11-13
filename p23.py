
num=int(input("enter number"))

for i in range (num+1):
    for j in range (num-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")

    print("")