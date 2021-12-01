import random


roll_again = 'yes'

while roll_again == "yes" or roll_again == "y":
    computer = []
    player = []
    print("rolling dice")
    for i in range(5):
        dice1 = random.randint(1, 6)
        computer.append(dice1)
        dice2 = random.randint(1, 6)
        player.append(dice2)
    print("computer rolled: ", computer)
    print("player rolled: ", player)
    com_o = computer.count(max(computer, key = computer.count))
    plyr_o = player.count(max(player, key = player.count))
    print("Computer has ", com_o, " of a kind")
    print("Player has ", plyr_o, " of a kind")
    if com_o > plyr_o:
        print("Computer wins")
    elif plyr_o > com_o:
        print("Player wins")
    else:
        print("It is a tie game")
    roll_again = input("Do you want to roll again? (yes/y) or (no/n)")
print("game ended")