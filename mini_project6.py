#. Character Checker Input a character
#Check:
#Vowel
#Consonant
#Digit

ch = input("Enter a character: ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
     print(ch,"is a vowel")
elif ch=='b' or ch=='c' or ch=='d' or ch=='f' or ch=='g' or ch=='h' or ch=='B' or ch=='C' or ch=='D':
     print(ch,"is a consonant")
else:
     print(ch,"is a digit")