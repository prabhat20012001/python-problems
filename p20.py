num1=int(input("first num"))
num2=int(input("second num"))
num3=int(input("third num"))

if(num1>num2 and num1>num3 ):
  print(num1)
elif(num2>num1 and num2>num3):
  print(num2)
else:
  print(num3)

  #==========
#   print(max(num1,num2,num3))