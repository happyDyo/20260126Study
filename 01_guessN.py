import random
import json

def guess_number() :

    print("\nWelcome to GuessN!\n")

    file_path = 'score.json'

    try :
        with open(file_path, 'r') as f :
            record = json.load(f)
            HS = record['Highest Score']

    except FileNotFoundError :
        print("You can be the Champion!!\n")
        HS = 99
        record = {'champion' : 'None', 'Highest Score' : HS}

    target = random.randrange(1,100)
    count = 0

    name = input("What's your name? : ")

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
                print("Highest Score is %s 's %d point" % (record['champion'], HS))
                if HS > count :
                    HS = count
                    print("\n==============================")
                    print("You are the New Champion!!\n")
                    print("Champion : %s, Score : %d" % (name, count))
                    print("==============================")
                    
                    nrecord = {'champion' : name, 'Highest Score' : count}
                    with open(file_path, 'w') as f :
                        json.dump(nrecord, f)
                else :
                    print("\nSo Closeeee...")
                break
            elif guess > target :
                print("Down!")
            else :
                print("Up!")
        except ValueError :
            print("Only Number")

        except KeyboardInterrupt :
            print("\nGood bye ~")
            break
        

guess_number()