lst=[]
for i in range(6):
    lst.append(int(input(f"enter {i } th number")))
print("This is the list:",lst)
sum=0
for i in range(6):
    sum+=lst[i]
print("sum:",sum)