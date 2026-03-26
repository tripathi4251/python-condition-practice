#Marks Analyzer Input 5 subject marks Print:
#Pass if all ≥ 40
#Else Fail

s1=int(input("Enter the marks of subject 1: "))
s2=int(input("Enter the marks of subject 2: "))
s3=int(input("Enter the marks of subject 3: "))
s4=int(input("Enter the marks of subject 4: "))
s5=int(input("Enter the marks of subject 5: "))

total=s1+s2+s3+s4+s5
percentage=(total/500)*100
print("Total marks: ",total)
print("Percentage: ",percentage)

if total>=40:
    print("Result: Pass")
else:
    print("Result: Fail")