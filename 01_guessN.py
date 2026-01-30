import random

def guess_number() :

    print("\nWelcome to GuessN!\n")

    try :
        f = open("score.txt", 'r')
        
        line = f.readline()
        print(line)
        HS = int(line.split(':')[1].strip())
        if not line :
            print("Can you break him out?\n")
        f.close()
    
    except FileNotFoundError:
        print("You can be the Champion!!\n")
        HS = 99

    target = random.randrange(1,100)
    count = 0

    while True :
        try :
            guess = int(input("guess?( exit -> 0 ) : "))
            count+=1
            if guess == 0 :
                print("Game Over..")
                break
            elif guess == target : 
                print("correct!\n")
                print("Your score is %d !!\n\n"%count) 
                print("Highest Score is %d" % HS)
                if HS > count :
                    HS = count
                    print("You are the New Champion!!")
                    f = open("score.txt", 'w')
                    data = "Highest Score : %d" % HS
                    f.write(data)
                    f.close()
                else :
                    print("So Closeeee...")
                break
            elif guess > target :
                print("Down!")
            else :
                print("Up!")
        except ValueError :
            print("Only Number")
        

guess_number()