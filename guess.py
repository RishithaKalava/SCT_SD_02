import random
guess=random.randint(1,9)
while True:
    num=int(input("Guess the number"))
    if num==guess:
        print("you are correct")
        break
    elif num>guess:
        print("your guess is high")
    else:
        print("your guess is low")
    print("guess again")
        
