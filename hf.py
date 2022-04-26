import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number:----"))
if userInput>Cnumber:
    print("computer number",Cnumber)
    print("Your guess Number is too high")
elif Cnumber>userInput:
    print("Your guess number is too low")
else:
    print("Your guess number is equal")
