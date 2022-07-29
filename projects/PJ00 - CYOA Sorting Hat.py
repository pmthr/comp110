# Create Your Own Adventure, Sorting Hat
import time
import random

# global variable declarations
points: int 
player: str

# emoji declarations
WICKEDWITCHES = "\U0001F9D9"
SLYTHERIN = "\U0001F40D"
HUFFLEPUFF = "\U0001F43E"
GRYFFINDOR = "\U0001F981"
RAVENCLAW = "\U0001F985"

def greet() -> None:
    # Greet method - welcome message, player name, emoji usage
    global player
    print(f"{WICKEDWITCHES} Welcome to the sorting ceremony, young wizard.")
    player = input(f"What is your name? {WICKEDWITCHES} ")

def main() -> None:
    # Main method
    greet()
    global points
    global player
    points = 0
    print(f"To make sure I do this right, {player}, type the number of your response choice. Are you nervous?")
    time.sleep(1)
    nerves: int = int(input("I'm terrified, but I'll stay put. | Of course not, I know why I'm here. | Yeah no I'm not doing this today, pick someone else! "))
    if nerves == 1:
        nervous()
    elif nerves == 3:
        print("I wish you were ready, but I understand. Speak to the headmaster, they'll tell you what to do next. Thank you for coming to Hogwarts, and farewell.")
        time.sleep(1)
        quit()
    time.sleep(0.5)
    points += quiz(points) 
    print(decision())
    conclusion()

def nervous() -> None: 
    # Custom procedure - directly updates global points variable, updates points per logical user response
    global points
    time.sleep(1)
    print("Fear not, child, I cannot hurt you. Tell me, what pet have you chosen for the school year?")
    time.sleep(0.5)
    print("You glance over to the table with all of your things.\nYou stutter: ")
    time.sleep(1)
    points += int(input("A toad | An owl | A cat "))
    time.sleep(1)
    print("A good choice. Are you here with friends?")
    time.sleep(1)
    points += int(input("Yes, they're sitting at the table. | I guess, I made some on the train. | No, I'm alone."))
    time.sleep(1)
    print("Whether you are alone or not, I am your friend, and Hogwarts is here to help. Lets begin, shall we?")
    time.sleep(0.5)
    
def quiz(quizpoints: int) -> int:
    # Custom function - uses parameter quizpoints, updates and returns quizpoints. the global points variable is then updated in main on line 43
    time.sleep(1)
    print("During final exam week, the common rooms are charmed to smell comforting. When you walk into yours, what would it smell like?")
    time.sleep(1)
    quizpoints += int(input("My mother's favorite herbal tea | Fresh, crisp parchment | A crackling log fire | The salty oceans "))
    time.sleep(1)
    print("Interesting. Now, it is not uncommon for the sounds of band practice to spill into the hallways. Which instrument brings a smile to your face?")
    time.sleep(1)
    quizpoints += int(input("Trumpet | Piano | Drum | Violin "))
    time.sleep(1)
    print("Good choice. Let's go away from Hogwarts for a minute. You have been traveling on a long road and finally reach a dividing path. Which path do you head towards? ")
    time.sleep(1)
    quizpoints += int(input("Leftmost, where dirt turns to stone, signs of a small town. | Slight left, to the fog-covered forest | Slight right, down the original path | Rightmost, where you can almost hear crashing waves. "))
    time.sleep(1)
    return quizpoints

def decision() -> str:
    # Another custom procedure, uses f-strings with player name and emojis but does not return/update global points
    global player
    global points
    print(f"Hmm. I think I have heard enough. {player}, welcome to...")
    time.sleep(1.5)
    if points > 14 and points <= 18:
        return f"{SLYTHERIN} SLYTHERIN! {SLYTHERIN}"
    elif points > 10 and points <= 14:
        return f"{GRYFFINDOR} GRYFFINDOR! {GRYFFINDOR}"
    elif points > 5 and points <= 10:
        return f"{RAVENCLAW} RAVENCLAW! {RAVENCLAW}"
    else:
        return f"{HUFFLEPUFF} HUFFLEPUFF! {HUFFLEPUFF}"

def conclusion() -> None:
    # Function for game loop, satisfaction leads to the end of the game and dissatisfaction leads to a game loop while updating user about the # of points
    global points
    satisfied: str = input("Are you satisfied with your house?\nType Y or N ")
    if satisfied == "Y":
        print("Wonderful. I wish you the best of luck during your time at Hogwarts. Pay me a visit someday!")
        time.sleep(1)
        quit()
    elif satisfied == "N":
        print(f"Whatever do you mean? You had {points} points!")
        time.sleep(0.5)
        print("You glare upwards.")
        time.sleep(0.5)
        print("Okay, fine. In rare occasions, I do make mistakes. Lets try again.")
        time.sleep(1)
        main()

if __name__ == "__main__":
    # Intimidation tactic using randint happens right before the game starts
    time.sleep(0.75)
    previous: int = random.randint(1, 100)
    if previous < 50:
        print("THIS FOOL....LANDED IN GRYFFINDOR! Anyways...")
    elif previous == 50:
        print("You're obviously in Ravenclaw. Have you seen yourself in those glasses? Nerd!")
    else:
        print("Don't take this the wrong way, but....SLYTHERIN!")
    time.sleep(1)
    print("NEXT PERSON PLEASE!")
    time.sleep(0.75)
    main()