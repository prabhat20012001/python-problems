pwd=input("enter apssword")

if(pwd.isalnum() and pwd.len()<=8):
    print("yes")
else:
    print("no")