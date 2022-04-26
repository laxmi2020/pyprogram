import random
l=["rock","scissor","paper"]

'''
rock vs paper->paper wins
rock vs scissor->rock wins
paper vs scissor->scissor wins.
'''

while True:
    UC=int(input('''
Game Start.....
1 Yes
2 No | Exit
    
    '''))
    if UC==1:
        for a in range(1,6):
            UserInput=int(input('''
            1 Rock
            2 Scissor
            3 Paper
            
            '''))
            if UserInput==1:
                uchoice="rock"
            elif UserInput==2:
                uchoice="Scissor"
            elif UserInput==2:
                uchoice="paper"
            Cchoice=random.choice(1)
            print(uchoice)
            print(Cchoice)
            if Cchoice==uchoice:
                print("computer value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("computer value", Cchoice)
                print("User value", uchoice)
                print("You Win")
                ucount = ucount + 1

            else:
                print("computer value", Cchoice)
                print("User value", uchoice)
                print("Computer Win")
                ccount = ccount + 1

        if ucount==ccount:
             print("Final Game Draw")
             print("User Score",ucount)
             print("Computer Score",ucount)
        elif ucount>ccount:
             print("Final You Win The Game....")
             print("User Score",ucount)
             print("Computer Score",ucount)
        else:
            print("Computer Win The Game....")
            print("User Score", ucount)
            print("Computer Score", ucount)

    else:
        break


