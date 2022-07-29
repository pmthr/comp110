# Program that outputs one of at least four random, good fortunes

from random import randint

print("Your fortune cookie says...")

fortune_number: int = randint(1, 4)
if fortune_number == 1:
    print("Someone special has their eye on you...")
else:
    if fortune_number == 2:
        print("You are beginning to understand your true power. Use it wisely.")
    else:
        if fortune_number == 3:
            print("Try and fail, but never fail to try.")
        else:
            if fortune_number == 4:
                print("A person cannot be comfortable without their own approval.")

print("Now, go spread positive vibes!")