# Libraries
import time, sys, random

# Functions
def missing_value():
    print("Incorrect or missing value!")

def add_dot():
    print("...")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print(".")
    time.sleep(1)

def play_again():
    again = input("Do you want to play again? (Yes: Y,y - No: N,n): ")
    if again == "Y" or again == "y":
        start_the_game()
    elif again == "N" or again == "n":
        quit_the_game()
    else:
        missing_value()
        play_again()

def quit_the_game():
    print("The game is ending")
    add_dot()
    sys.exit()

# Classes
class Player:
    def __init__(self, name, health=10, power=100, point=0):
        self.name = name
        self.health = health
        self.power = power
        self.point = point

    def give_info(self):
        print(f"""
        Name = {self.name}
        Health = {self.health}
        Power = {self.power}
        Point = {self.point}
        """)

    def attack(self, enemy):
        count = self.attack_defend_count()
        print("Attack started")
        add_dot()
        if count == 1:
            print("Attack successful!")
            self.power -= 8
            self.point += 10
            enemy.health -= 2
        else:
            print("Attack failed!")
            self.power -= 8
            self.health -= 1
            enemy.point += 8
        self.give_info()
        enemy.give_info()

    def defend(self, enemy):
        count = self.attack_defend_count()
        print("Defense started")
        add_dot()
        if count == 1:
            print("Defense successful!")
            enemy.power -= 8
            self.point += 10
            enemy.health -= 1
        else:
            print("Defense failed!")
            enemy.power -= 8
            self.health -= 1
            enemy.point += 10
        self.give_info()
        enemy.give_info()

    def attack_defend_count(self):
        return random.randint(1, 2)

# Starting a Game
def start_the_game():
    global player1, computer
    player1 = Player("You")
    computer = Player("Computer")

    print("The Game Begins")
    add_dot()

    turn = "player"

    while True:
        if turn == "player":
            move = input("""
            1 - Attack
            2 - Defend
            3 - Exit
            Move selection: 
            """)

            if move == "1":
                player1.attack(computer)
            elif move == "2":
                player1.defend(computer)
            elif move == "3":
                quit_the_game()
            else:
                missing_value()
                continue

            turn = "computer"

        else:
            move = random.choice(["1", "2"])
            print(f"Computer chose move: {move}")

            if move == "1":
                computer.attack(player1)
            elif move == "2":
                computer.defend(player1)

            turn = "player"

        # Game end control
        if player1.point >= 100 or computer.health <= 0 or computer.power <= 0:
            print("Congratulations! You won the game.")
            play_again()
            break

        if computer.point >= 100 or player1.health <= 0 or player1.power <= 0:
            print("Computer won the game.")
            play_again()
            break

# Starting the game
start_the_game()