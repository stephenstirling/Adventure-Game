import os
import random
import sys
import time

player_name = (input("Before we begin, please enter your name: "))


# # Classes

class Player:

    def __init__(self):
        self.name = player_name
        self.health = 100
        self.gold = 100
        self.magic_points = 100
        self.weapon = wep_selection()


def attack_enemy(self, enemy):
    while enemy.health > 0:
        if you.weapon == "sword":
            enemy.health = enemy.health - random.randint(1, 20)
        if you.weapon == "spear":
            enemy.health = enemy.health - random.randint(1, 30)
        if you.weapon == "axe":
            enemy.health = enemy.health - random.randint(1, 40)
        print("The strike the enemy! Their health is now {}".format(enemy.health))
    print("You have defeated a monster and as a reward you get +10 health!")
    self.health = + 10
    print("You have {} health".format(self.health))


def escape():
    print("To successfully escape, you need to guess the number of the die properly!\n")
    actual_num = random.randint(1, 7)
    guess = int(input("Take a guess: "))
    if guess == actual_num:
        print("You are right!\n")
        print("You have escaped successfully!\n")
    else:
        print("You are wrong! Now you must prepare for battle!\n")


def block(defender, enemy_weapon):
    actual_number = random.randint(0, 4)
    print("Guess a number one to four\n")
    guess = int(input("> "))
    if guess == actual_number:
        print("You have successfully blocked the attack")
        pass
    else:
        defender.health -= enemy_weapon.damage  # 01/03 this needs to be fixed properly


class Enemy:

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


you = Player("you", 100)
goblin = Enemy("Goblin", 50)
troll = Enemy("Troll", 50)
orc = Enemy("Orc", 50)
sword = Weapon("sword", 3)
spear = Weapon("spear", 2)
axe = Weapon("axe", 4)


### Menu Screen Selection
def menu_screen_options():
    selection = input("> ")
    if selection.lower() == ("play"):
        start_game()  # place holder until ready
    elif selection.lower() == ("exit"):
        sys.exit()
    while selection.lower() not in ['play', 'quit']:
        print("Please enter a valid argument")
        selection = input("> ")
        if selection.lower() == ("play"):
            start_game()  # place holder until ready
        elif selection.lower() == ("exit"):
            sys.exit()


def start_game():
    return


### Menu Screen
def menu_screen():
    os.system('clear')
    print('#####################')
    print('Adventures in Lebedyn')
    print('#####################')
    print('      - Play -       ')
    print('      - Exit -       ')
    menu_screen_options()  # this returns the player to the title screen after their selection


### Game Controls

def user_prompt():
    print("\n + =========")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ["buy", "attack", "defend", "look", "read", "rest", "interact"]
    while action.lower().strip() not in acceptable_actions:
        print("You need to pick a new options, please try again.\n")
        action = input("> ")


## Game Fuctions


### 01/02 I need to figure out how to exit from the if statement if successful, and return to the battle

### Weapon Selection
def wep_selection():
    weapon_options = ["sword", "spear", "axe"]
    print("\n + =========")
    print("""Welcome, {}. Before you begin your journey, please choose from one of the following three weapons:

                1) Sword
                2) Spear
                3) Axe
                """.format(player_name))
    action = input("> ")
    while action.lower().strip() not in weapon_options:
        print("Please choose one of the weapons")
        action = input("> ")

    if action == weapon_options[0]:
        y = "sword"
        return y

    elif action == weapon_options[1]:
        y = "spear"
        return y

    elif action == weapon_options[2]:
        y = "axe"
        return y


### Game Intro (Paths)

def intro():
    path_options = ["1", "2", "3"]
    x = ""
    while x not in path_options:
        print("""You are about to begin a very long journey. Ahead of you lie three paths:

          1) The shortest path. This path has the most amount of monsters
          2) The medium path. This path has an average amount of monsters.
          3) The longest path. This path has the least amount of monsters.
           """.format(player_name))

        x = (input("Please select a path (1,2,3): "))
        # print("You have selected " + x)
    if x == path_options[0]:
        path1()
    elif x == path_options[1]:
        path2()
    elif x == path_options[2]:
        path3()


### Game Paths

def path1():
    print("You have chosen the shortest path. You start walking but after a few hours the shadows start getting longer")
    time.sleep(1)
    print(
        "Suddenly, a wizard jumps out of the underbrush! He pulls out a dice and asks you to pick a number one "
        "through six! He warns you, depending on your guess that a monster could be summoned!")
    guess = int(input("Take a guess: "))
    actual_num = random.randint(1, 7)
    if guess != actual_num:
        # while goblin.health >= 0 or you.health >= 0:
        print("Suddenly a wild goblin appears!")
        time.sleep(1)
        print("The goblin prepares to swing his axe at you!\n")
        print("Would you like to try to block the attack or escape?")
        choices = ["block", "escape"]
        choice = input("> ")
        while choice.lower().strip() not in choices:
            print("You need to pick a new option, please try again.\n")
            choice = input("> ")
            if choice.lower().strip() == "escape":
                escape()
            else:
                block(Player, goblin)

        goblin.attack_by_enemy(you)
        print("The goblin attacks you and now you have {} health".format(you.health))
        you.attack_enemy(goblin)
    else:
        if goblin.health <= 0:
            print("You have defeated the goblin and as a reward get 5 gold.")
            you.gold += 5
        elif you.health <= 0:
            print("You have been defeated! This is the end of the game")

    time.sleep(1)
    print("You continue on traveling for a while until you reach a clearing.")
    time.sleep(1)
    print("You encounter a magician. He asks if you would like to increase your health by 10 points for 10 gold?")

    while user_decision == "yes" or "no":
        user_decision = input("Would you like to buy more health?: ")
        if user_decision == "yes":
            buy_health(you)
        else:
            print("You continue on your way")

    time.sleep(1)
    print(
        "After walking for a while longer, you decide to take a rest. You are awaken by a thief trying to steal your gold.")
    theif_options = ["give", "fight"]
    z = ""
    while second_choice not in theif_options:
        second_choice = input(
            "Would you like to fight the thief or give them your gold? Please enter 'give' or 'fight'")
        if second_choice == "give":
            you.gold = 0
        elif second_choice == "fight":
            while troll.health >= 0 or you.health >= 0:
                troll.attack_by_enemy(you)
                print("The troll attacks you and now you have {} health".format(you.health))
                you.attack_enemy(troll)


def path2():
    print("You have chosen the middle path. You walk for a while without encountering any monsters")
    time.sleep(1)
    print("All of a sudden a rather large monster jumps out!")
    time.sleep(1)
    choice = input("""You now decide to fight or run! Please type "run" or "fight": """)
    if choice == "run":
        print("You dart pass the monster and escape with your life!")
    elif choice == "fight":
        path2_monster.major_attack(you)
        print("You lose all your health!")
        time.sleep(1)
        print("Your journey ends here!")
    else:
        print("You did not type an acceptable response")
        path2()


def path3():
    print("You walk for many days until you come to a river. You notice there is a bridge going across the river")
    time.sleep(1)
    print(
        "As your approach there bridge, a troll appears from underneath the bridge. He says that you must correctly answer this question to go across the bridge!")
    time.sleep(1)
    guess = int(input("""How many Oscars did the film "Return of the King" win in 2003?: """))
    correct_answer = 11
    if guess == correct_answer:
        print("That is correct and you make cross")
    else:
        print("Suddenly a wild dragon appears! You reach for your {} and fire!".format(weapon))
        shot = int(input("Enter a number between 1 and 3 to determine if your shot hits!"))
        hit = random.randint(1, 4)
        if shot == hit:
            print("You shot hits the dragon and you are able to make it home!")


def play_again():
    x = input("""Would you like to play again. Please enter "yes" or "no": """)
    if x == "yes":
        Intro()
    elif x == "no":
        print("Thank you for playing and have a great day !")
    else:
        print("You did not enter a valid response!")
        play_again()


def buy_health(person):
    person.gold = person.gold - 10
    person.health = person.health + 10


# # Main Programs
Intro()
play_again()
