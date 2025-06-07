import random 
num=random.randint(1,10)
count=0
max_count=3
while count<max_count:
    
    
    try:
        guess=int(input(("guess a number between 1 to 100 : ")))
        if guess==num:
            

            break
            print("attempts completed")
        elif guess>num:
            print("guessed number is too high!!")
            count+=1
        elif guess<num:
            print("guessed number is too low!!")
            count+=1
        else:
            pass
    except ValueError:
        print("please enter a valid number")
        count-=1
    if max_count==count:
        print("limit exceeded")