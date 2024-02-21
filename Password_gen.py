from time import sleep as wait
import sys
import string
import random


def cool_pass(target, guess, fixed):
    while target != guess:
        while True:
            i = random.randint(0, len(target) - 1)
            if i not in fixed:
                break

        j = random.randint(32, 127)
        guess = guess[:i] + chr(j) + guess[i + 1 :]
        if guess[i] == target[i]:
            fixed.add(i)

        sys.stdout.write(f"\n{guess}")  # \n maybe
        sys.stdout.flush()
        wait(0.0005)


def password_gen(lenght=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chr = "!@#$%&*-=_+|;:,./?"
    all_chr = letters + digits + special_chr

    password = "".join(random.choice(all_chr) for i in range(lenght))
    return password


target = password_gen()
guess = "0" * len(target)
fixed = set()
cool_pass(target, guess, fixed)

print("\nThere is a Strong Password For You")

##COOL PASSWORD GENERATOR
