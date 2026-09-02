import random 

secret_number = random.randint(1, 100)
attempts = 0

while True :
    guess = int (input("guess the number: "))
    attempts += 1

    if secret_number == guess :
        print("Correct!")
        break

    elif guess > secret_number :
        print("Too High!")

    else:
        print("Too Low!")

print(f"your guessed it in {attempts} attempts.")
