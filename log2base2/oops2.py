class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
c1=Customer("Nitish",34)
c2=Customer("Nitishva",36)
c3=Customer("Nitish kr",38)

L=[c1,c2,c3]

for i in L:
    print(i)
    print(i.name,i.age)