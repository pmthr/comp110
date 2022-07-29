# An exercise in remainders and boolean logic
# Tar Heels

choice: int = int(input("Enter an int: "))
toprint: str = ""

if choice % 2 == 0 and choice % 7 == 0:
    print("TAR HEELS")
elif choice % 2 == 0 and choice % 7 != 0:
    print("TAR")
elif choice % 7 == 0 and choice % 2 != 0:
    print("HEELS")
else:
    print("CAROLINA")

# Drawing forests in a loop
# Happy Trees

TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0
j: int = 0
trees: str = ""

if depth > 0:
    while i < depth - 1:
        trees += TREE
        print(trees)
        i += 1
    print(trees + TREE)

# Repeating a beat in a loop
# Repeat Beat

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 0
beat_repeated: str = ""

if repeat > 0:
    while i < repeat - 1:
        beat_repeated = beat_repeated + beat + " "
        i = i + 1
    print(beat_repeated + beat)
else:
    print("No beat...")