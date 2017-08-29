from random import randint

#create random integer
x = randint(1,9)
correct = False

#while loop for number of guesses
while not correct:
    y = int(input("Try to guess my number:"))
    if y == x:
        print ("You are correct!")
        correct == True
        break;
    if y < x:
        print ("Your guess is too low. Please guess again")
    if y > x:
        print ("Your guess is too high. Please guess again.")