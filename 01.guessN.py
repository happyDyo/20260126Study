import random

def guess_number() :
    target = random.randrange(1,100)

    while True :
        try :
            guess = int(input("guess?( exit -> 0 ) : "))
            if guess == 0 :
                print("Game Over..")
                break
            elif guess == target : 
                print("correct")
                break
            elif guess > target :
                print("Down!")
            else :
                print("Up!")
        except ValueError :
            print("Only Number")
        

guess_number()