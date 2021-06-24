import random

number=random.randint(1,9)
print(number)

playerName=input("Hello, what's your name?")
numberOfChances=0
print('OK'+playerName+'I am guessing a number between 1 and 9:')

while numberOfChances < 5:
     guess=int(input())
     numberOfChances+=1
    if guess < number:
        print('Your guess is too low')
    
    elif guess > number:
        print('Your guess is too high')

    if guess == number:
        print("Congrats YOU WON")
        break
    
    else:
    print("YOU LOSE!! The number is",number)




