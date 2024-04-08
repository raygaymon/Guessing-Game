from random import randint

answer = randint(0, 100)
attempts = 0
guess = None
difference = answer

while (answer != guess):
    guess = int(input("Guess the answer: "))
    if guess == answer:
        print(f"Yay you did it!\nYou took {attempts} tries to get the answer")
        break
    else:
        if attempts > 0:
            newDiff = abs(guess - answer)
            if newDiff > difference:
                print("Colder")
            else :
                difference = newDiff
                print("Warmer")
        else:
            difference = abs(guess - answer)
            if difference < 11:
                print("WARM")
            else:
                print("COLD")
    attempts += 1
    

