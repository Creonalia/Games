import random

playing = True

while playing:
    number = random.randint(1, 100)
    guess = input("Guess an integer between 1 and 100.\n")

    while True:
        try:
            guess = int(guess)
        except:
            guess = input("That's not an integer. Try again.\n")
            continue

        if guess > 100 or guess < 1:
            guess = input("It's between 1 and 100. Try again.\n")
        elif guess == number:
            break
        elif guess > number:
            guess = input("Too high. Try again.\n")
        else:
            guess = input("Too low. Try again.\n")

    playing = input("Correct! Would you like to play again? Yes/No.\n").lower() == "yes"
    
print("Thanks for playing!")    
