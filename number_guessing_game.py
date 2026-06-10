import random

def valid_input(prompt):
    guess = 0
    while guess not in range(1, 4):
        try:
            guess = int(input(prompt))
        except ValueError:
             print("Please enter a digit [1, 2, 3].\n")
    return guess

def play_game():
     
    number = random.randint(1, 100)

    won = False

    print("This is Guess the Number.\nI'm thinking of a number " \
    "between 1 and 100.\nYou have 5 chances to guess the correct number.\n" \
    "Please select the difficulty level:\n\n1. Easy (10 chances)\n" \
    "2. Medium (5 chances)\n3. Hard (3 chances)\n\n")
    difficulty_select = valid_input("Enter your choice: ")

    if difficulty_select == 1:
        difficulty = "Easy"
        guesses = 10
    elif difficulty_select == 2:
        difficulty = "Medium"
        guesses = 5
    elif difficulty_select == 3:
        difficulty = "Hard"
        guesses = 3
    else:
        print("Please select a digit [1, 2, 3].")

    print(f"Great! You have selected the {difficulty} difficulty!\n")

    for i in range(guesses):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except ValueError:
             print("Please enter a digit.\n")
        
            
        if guess > number:
            print("Lower!\n")
        elif guess < number:
            print("Higher!\n")
        elif guess == number:
            print(f"Correct! The number was {number}!")
            won = True
            break
         

    if won == False:
        print(f"You ran out of guesses! The number was {number}!\n")
    
    play_again = input("Would you like to play again? [Y/N]: ").lower()

    while play_again not in('y','n'):
        play_again = input("Enter [Y/N]: ").lower()

    if play_again == 'y':
        play_game()

play_game()
        


          
          
