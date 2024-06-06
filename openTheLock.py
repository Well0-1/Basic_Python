import random

lock = str(random.randint(100, 999))


def clues(guess, lock):
    correct_place, wrong_place, notEx = 0, 0, 0

    for i in range(3):
        if guess[i] == lock[i]:
            correct_place += 1
        elif guess[i] in lock:
            wrong_place += 1
        else:
            notEx += 1
    print("----------------------------------------------------")
    if correct_place:
        print(f"{correct_place} Digit is right and in its place")
    if wrong_place:
        print(f"{wrong_place} Digit is right but in the wrong place")
    if notEx:
        print(f"{notEx} Digit is wrong")
    print("----------------------------------------------------")


def unlock(lock):
    trys = 0
    while True:
        trys += 1
        guess = input("3 Basamaklı bir sayı giriniz: ")

        while not guess.isdigit() or len(guess) != 3:
            print("3 Basamaklı bir Sayı girmelisiniz!")
            guess = input("3 Basamaklı bir sayı giriniz: ")

        if guess == lock:
            print(f"Congratulations! You managed to unlock it in {trys} try")
            break
        else:
            clues(guess, lock)


unlock(lock)
