while True:
    import random
    lst=[1,2,3,4,5,6]
    choice=input("roll a dice? (y/n) : ").lower()
    if choice == "y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"({die1},{die2})")
    
    elif choice == "n":
        print("thanks for  playing")
        break
    else:
        print("invalid option!!!")
    