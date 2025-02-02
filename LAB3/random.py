import random
secret_number = random.randint(1,20)
name = input("Hello! What is your name?\n")
print(f"\nwell, {name}, i am thinking of a number between 1 and 20.")
attempts=0
while True:
    guess=int(input("Take a guess.\n"))
    attempts+=1
    if guess<secret_number:
        print("Your guess is too low")
    elif guess >secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {attempts} guesses! ")
        break