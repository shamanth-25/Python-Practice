import random
n=random.randrange(1,10)
guess=int(input("Enter any number: "))
while n!=guess:
    if guess<n:
        print("Too low")
        guess=int(input("Enter number again: "))
    elif guess>n:
        print("Too High")
        guess=int(input("Enter number again:"))
    else:
        break
print("You guessed is right!!")