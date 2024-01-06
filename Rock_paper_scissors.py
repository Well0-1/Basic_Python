import random

def computer_choice() :
    c_choice = random.choice(["Rock","Paper","Scissors"])
    return c_choice
    
def user_choice() :
    trys = 5
    u_choice = input("Choose 'Rock' (R), 'Paper' (P), or 'Scissors' (S) or Press (Q) to Quit: ").lower()
    while u_choice not in ["r","p","s","q"] :
        print("Unvalid Argument, You must enter R,P,S or Q")
        u_choice = input("Choose 'Rock' (R), 'Paper' (P), or 'Scissors' (S) or Press (Q) to Quit: ").lower()
        trys -= 1
        if trys == 0 :
            print("Too Many Failed Attempts, Shutting Down...")
            quit()
    return u_choice
    
def game() :
    c_points = 0
    u_points = 0
    raund_num = input("How many raunds you want to play: ")
    while not raund_num.isdigit():
        print("You must enter an integer")
        raund_num = input("How many raunds you want to play: ")
    raund_num = int(raund_num)
        
    for i in range(raund_num):
        print(f"Raund {i+1}")
        u_choice = user_choice()
        c_choice = computer_choice()
        if (c_choice == "Rock" and u_choice == "p") or (c_choice == "Paper" and u_choice == "s") or (c_choice == "Scissors" and u_choice == "r") :
            print(f"You won this round, Computer Choosed: {c_choice}")
            u_points +=1
        elif (c_choice == "Paper" and u_choice == "r")  or (c_choice == "Scissors" and u_choice == "p") or (c_choice == "Rock" and u_choice == "s") :
            print(f"Computer won this round, Computer Choosed: {c_choice}")
            c_points += 1 
        else : 
            print("Tie!")
    
    if u_points > c_points :
        print(f"Congratulations You Won!\n----Score----\nYou:{u_points}\nComputer: {c_points}")
    elif u_points < c_points : 
        print(f"Unfortunately You Lost!\n----Score----\nYou: {u_points}\nComputer: {c_points}")
    else :
        print(f"Game's Over, Draw!!\n----Score----\nYou: {u_points}\nComputer: {c_points}")

game()
