##print following pattern

num=int(input("enter number"))
for i in range(num):
    for j in range(i):
        print("*",end="")
    print("")