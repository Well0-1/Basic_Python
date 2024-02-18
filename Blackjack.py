import random as Dealer
from time import sleep as wait

values = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "A": 11,
    "K": 10,
    "Q": 10,
    "J": 10,
}


Deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4

Dealer.shuffle(Deck)


def player(Deck):
    Hand = []
    for i in range(2):
        card = Deck.pop()
        Hand.append(card)
    return Hand


def dealer_h(Deck):
    dealer_hand = []
    for i in range(2):
        card = Deck.pop()
        dealer_hand.append(card)
    hidden_card = dealer_hand[0]
    dealer_hand[0] = "Hidden"
    return dealer_hand, hidden_card


def point(player_hand):
    ace_flag = False
    points = 0
    for i in player_hand:
        for k, v in values.items():
            if k == i:
                points += v
                if any(c == "A" for c in player_hand) and points > 21 and not ace_flag:
                    points -= 10
                    ace_flag = True
                elif points > 21:
                    print("BUST! Dealer Wins.")
                    quit()
    return points


def dealer_p(dealer_hand):
    ace_flag = False
    points = 0
    for i in dealer_hand:
        for k, v in values.items():
            if k == i:
                points += v
                if any(c == "A" for c in dealer_hand) and points > 21 and not ace_flag:
                    points -= 10
                    ace_flag = True
                elif points > 21:
                    print("Dealer BUSTS!\nYou Won!")
    return points


def game():
    player_hand = player(Deck)
    dealer_hand, hidden_card = dealer_h(Deck)

    print(f"Your Hand = {player_hand}\nDealer's Hand = {dealer_hand}")

    choice = input("Do You Want to Hit or Stay?").capitalize()
    while not choice in ["H", "S", "Stay", "Hit"]:
        print("You Have to Enter Your Move!")
        choice = input(
            "Do You Want to Hit or Stay? İf You Want to Quit Enter 'Q'"
        ).capitalize()
        if choice == "Q":
            print("Have a Nice Day!")
            quit()

    while choice in ["H", "Hit"]:
        card = Deck.pop()
        player_hand.append(card)
        print(f"You Hit {card}\nYour Hand {player_hand}")
        wait(0.5)
        user_point = point(player_hand)
        if user_point == 21:
            print("Blackjack! Waiting For The Dealer...")
            dealer_hand[0] = hidden_card
            wait(0.5)
            print(
                f"Dealer Reveals the Hidden Card... It's {hidden_card}\nDealer's Hand = {dealer_hand}"
            )
            dealer_point = dealer_p(dealer_hand)
            while dealer_point < user_point:
                wait(1)
                card = Deck.pop()
                print(f"Dealer Hits... And Card is {card}")
                dealer_hand.append(card)
                wait(1)
                print(f"Dealer's Hand {dealer_hand}")
                wait(0.5)
                dealer_point = dealer_p(dealer_hand)
            if dealer_point == 21:
                print("Draw!")
                quit()
            elif dealer_point > 21:
                print("You Won!")
                quit()
        elif len(player_hand) == 5 and user_point <= 21:
            print("5 Card Trick!")
            while not len(dealer_hand) == 5:
                dealer_hand[0] = hidden_card
                print(
                    f"Dealer Reveals the Hidden Card... It's {hidden_card}\nDealer's Hand = {dealer_hand}"
                )
                wait(1)
                card = Deck.pop()
                print(f"Dealer Hits... And Card is {card}")
                dealer_hand.append(card)
                wait(1)
                print(f"Dealer's Hand {dealer_hand}")
                wait(0.5)
                dealer_point = dealer_p(dealer_hand)
                if dealer_point > 21:
                    print("You Won")
                    quit()
            if dealer_point > user_point:
                print(
                    "Dealer Wins! My Advice, You Really Should Check This Website https://quickabdest.com"
                )
                quit()
            elif dealer_point == user_point:
                print(
                    "Draw! My Advice, You Really Should Check This Website https://quickabdest.com"
                )
        choice = input("Do You Want to Hit or Stay?").capitalize()

    if choice in ["S", "Stay"]:
        user_point = point(player_hand)
        dealer_hand[0] = hidden_card
        print(
            f"Dealer Reveals the Hidden Card... It's {hidden_card}\nDealer's Hand = {dealer_hand}"
        )
        dealer_point = dealer_p(dealer_hand)
        if dealer_point > user_point:
            print("Dealer Won!")
            quit()
        elif dealer_point == user_point and dealer_point > 17:
            print("Draw!")
            quit()
        while dealer_point < user_point:
            card = Deck.pop()
            print(f"Dealer Hits {card}")
            wait(1)
            dealer_hand.append(card)
            print(f"Dealer's Hand  = {dealer_hand}")
            dealer_point = dealer_p(dealer_hand)
            if dealer_point > user_point and dealer_point <= 21:
                print("Dealer Wins!")
                quit()
            elif dealer_point == user_point:
                print("Draw!")
                quit()


game()
