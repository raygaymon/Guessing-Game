from random import randint

answer = randint(0, 100)
attempts = 0
badAttempt = 0
guess = None
difference = answer

while (answer != guess):
    guess = input("Welcome to the Guessing Game. Try to guess the answer from 1 - 100: ")

    if guess == "":
        continue
    else:
        guess = int(guess)

    if guess < 1 or guess > 100:
        if badAttempt > 0:
            print("Are you stupid")
        else :
            print("Please do not try to be funny. The range was already clearly stated")
        badAttempt += 1
        continue

    if guess == answer:
        print(f"Yay you did it!\nYou took {attempts} tries to get the answer")
        break
    else:
        if attempts > 0:
            newDiff = abs(guess - answer)
            if newDiff > difference:              
                print("Colder")
            else :
                print("Warmer")
            difference = newDiff
        else:
            difference = abs(guess - answer)
            if difference < 11:
                print("WARM")
            else:
                print("COLD")
    attempts += 1
    

