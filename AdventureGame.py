import random
import time
import cmd
import sys
import os



name = (input("Before we begin, please enter your name: "))

# Player Class
class player:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.magic = 50
        self._status_effects = []

thePlayer = player()

# Menu Screen Selection
def menu_screen_options():
    selection = input("> ")
    if selection.lower() == ("play"):
        start_game() # place holder until ready
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

# Menu Screen
def menu_screen():
    os.system('clear')
    print('#####################')
    print('Adventures in Lebedyn')
    print('#####################')
    print('      - Play -       ')
    print('      - Exit -       ')
    menu_screen_options()   # this returns the player to the title screen after their selection


# Weapon Selection
def WepSelection():
    weapon_options = ["1", "2", "3"]
    y = ""
    while y not in weapon_options:
        print("""Welcome, {}. Before you begin your journey, please choose from one of the following three weapons:

            1) Sword
            2) Spear
            3) Axe
            """.format(name))

        y = input("Please pick a weapon by entering the corresponding number(1, 2, or 3): ")

    if y == weapon_options[0]:
        y = "sword"
        return y

    elif y == weapon_options[1]:
        y = "spear"
        return y

    elif y == weapon_options[2]:
        y = "axe"
        return y


weapon_selected = WepSelection()

def Intro():
    path_options = ["1", "2", "3"]
    x = ""
    while x not in path_options:
        print("""Thank you for picking. You are about to begin a very long journey. Ahead of you lies three paths:

          1) The shortest path. This path has the most amount of monsters
          2) The medium path. This path has an average amount of monsters.
          3) The longest path. This path has the least amount of monsters.
           """.format(name))

        x = (input("Please select a path (1,2,3): "))
        #print("You have selected " + x)
    if x == path_options[0]:
        path1()
    elif x == path_options[1]:
        path2()
    elif x == path_options[2]:
        path3()


def path1():
    print("You have chosen the shortest path. You start walking but after a few hours the shadows start getting longer")
    time.sleep(1)
    print("Suddenly, a wizard jumps out of the underbrush! He pulls out a dice and asks you to pick a number one through six! He warns you, depending on your guess that a monster could be summoned!")
    guess = int(input("Take a guess: "))
    actual_num = random.randint(1, 7)
    if guess != actual_num:
        while goblin.health >= 0 or you.health >= 0:
            print("Suddenly a wild goblin appears!")
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
    print("After walking for a while longer, you decide to take a rest. You are awaken by a thief trying to steal your gold.")
    theif_options = ["give", "fight"]
    z = ""
    while second_choice not in theif_options:
        second_choice = input("Would you like to fight the thief or give them your gold? Please enter 'give' or 'fight'" )
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
    print("As your approach there bridge, a troll appears from underneath the bridge. He says that you must correctly answer this question to go across the bridge!")
    time.sleep(1)
    guess = int(input("""How many Oscars did the film "Return of the King" win in 2003?: """))
    correct_answer = 11
    if guess == correct_answer:
        print("That is correct and you make cross")
    else:
        print("Suddenly a wild dragon appears! You reach for your {} and fire!".format(weapon))
        shot = int(input("Enter a number between 1 and 3 to determine if your shot hits!"))
        hit = random.randint(1,4)
        if shot ==  hit:
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








# # Classes

class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.gold = 100
        self.weapon = weapon_selected



    def attack_enemy(self, enemy):
        while enemy.health > 0:
            if you.weapon == "sword":
                enemy.health = enemy.health - random.randint(1, 20)
            if you.weapon == "spear":
                enemy.health = enemy.health - random.randint(1, 30)
            if you.weapon == "bow_arrow":
                enemy.health = enemy.health - random.randint(1, 40)
            print("The strike the enemy! Their health is now {}".format(enemy.health))
        print("You have defeated a monster and as a reward you get +10 health!")
        self.health =+ 10
        print("You have {} health".format(self.health))






class Enemy:

    def __init__(self, name, health):
        self.name = name
        self.health = health




    def attack_by_enemy(self, character):
            if self.name == goblin:
                character.health = character.health - random.randint(0,20)
            if self.name == troll:
                character.health = character.health - random.randint(0, 30)
            if self.name == ork:
                character.health = character.health - random.randint(0, 40)

            print("You have died and that is the end of the game!")





class Weapon:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


you = Character("you", 100)
goblin = Enemy("Goblin", 100)
troll = Enemy("Troll", 100)
ork = Enemy("Ork", 100)
sword = Weapon("sword", 3)
spear = Weapon("spear", 2)
bow_arrow = Weapon("bow and arrow", 4)



# # Main Programs
Intro()
play_again()



