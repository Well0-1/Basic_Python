import random
import time
    
def game():
    start = time.perf_counter()
    min_number = int(input("Enter the minimum number of the range: "))
    max_number = int(input("Enter the maximum number of the range: "))
    
    computer_choice = random.randint(min_number,max_number)
    trys = 0
    while True:
        user_guess = int(input(f"Guess The Number Between {min_number} And {max_number} : "))
        trys += 1

        if user_guess == computer_choice :
            end = time.perf_counter()
            print(f"Congratulations, You Guessed the Number Correctly in {trys} trys! Game Time = {int((end-start)/60)} minutes {int((end-start)%60)} seconds")
            playAgain = input("Do You Want to Play Again? : ").capitalize()
            if playAgain in ["Yes","Y","E","Evet"]:
                game()
            else :
                break
                
        elif user_guess > computer_choice :
            print("The Number is Lower Than Your Guess")
            continue
        
        elif user_guess < computer_choice :
            print("The Number is Higher Than Your Guess")
            continue
        

game()