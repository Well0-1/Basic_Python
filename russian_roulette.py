import random as gun

bullet = gun.randint(0, 6)

while True:
    input("Press Enter to Pull the Trigger")
    if bullet == 0:
        print("You Died!")
        break
    else:
        print("It's Your Lucky Day!")
        bullet -= 1
