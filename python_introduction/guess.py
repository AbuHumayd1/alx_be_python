import random
for i in range(10):
    secret_number = random.randint(1, 5)
    guess = int(input("Guess a number between 1 and 5: "))

    match guess:
        case _ if secret_number == guess:
            print("Congratulations! You guessed the secret number.")
        case _ if secret_number < guess:
            print("Too high! Try again")
        case _ if secret_number > guess:
            print("Too low! Try again")
        case _:
            print(f"Sorry, the secret number was {secret_number}. Better luck next time!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank You")
        break