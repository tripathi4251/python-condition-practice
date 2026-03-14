#number guessing game
num =50
guess=int(input("guess a number"))
if (guess==num):
    print("correct")
elif (guess>num):
    print("too high")
elif(guess<num):
    print("too low")