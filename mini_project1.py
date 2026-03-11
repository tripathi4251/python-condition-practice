# simple calculator take two number perform calculation

num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
op=input("enter a operator (+,-,*,/):")
if (op=="+"):
    print("result:",num1+num2)
elif (op=="-"):
    print("result:",num1-num2)
elif (op=="*"):
    print("result:",num1*num2)
elif (op=="/"):
    print("result:",num1/num2)