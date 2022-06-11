

import random

answer = random.randint(1,9)

# we need to give 5 chances to the user

counter = 1

print("welcome to the guessing game!")
print("----------------------------------")

while(counter <= 5):

    useranswer = int(input("Guess a number from 1-9 : "))
    
    if useranswer > answer: 
        print("too high")
        
    elif useranswer < answer:
        print("too low")

    elif useranswer == answer:
        print("correct")
        break

    counter = counter + 1


if counter > 5 :
    print("You Lose!")


