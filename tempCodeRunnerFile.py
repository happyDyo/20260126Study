import random

def guess_number() :
    target = random.randrange(1,100)

    while(1) :
        guess = int(input("guess? : "))
        if(guess == target) : 
            print("correct")
            break
        else :
            if(guess > target) :
                print("Down!")
            else(guess < target) :
                print("Up!")

guess_number()