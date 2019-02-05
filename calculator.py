print("calculator program")
print("Add:1,sub:2,mul:3,div:4")
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
choice=input("enter your choice(1,2,3,4):")
if (choice==1):
  ans=num1+num2
  print(ans)
elif(choice==2):
  ans=num1-num2
  print(ans)
elif(choice==3):
  ans=num1*num2
  print(ans)
elif(choice==4):
    if num2==0:
      print("division by zero can't be done")
    else:
        ans=num1/num2
        print(ans)
else:
  print("invalid input")
