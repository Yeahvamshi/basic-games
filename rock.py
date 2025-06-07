#rock paper scissor
import random 
while True:
    options=["r","p","s"]
    comp=random.choice(options)
    user_choice=input("rock,paper,scissor(r,p,s) :").lower()
    print("enter a valid input ")
    print(f"you chose {user_choice}")
    print(f"computer chose {comp}")
    if ((user_choice == 'r' and comp =='s') or (user_choice== "s" and comp =='p') or  (user_choice == "p" and comp=="r")) :
        print("congo you wonn!!!")
    elif user_choice==comp:
        print("its a tie")
    else:
        print("haha failure mf ")