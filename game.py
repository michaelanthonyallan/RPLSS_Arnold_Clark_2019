from random import choice

ROCK, PAPER, LIZARD, SCISSORS, SPOCK = 1, 2, 3, 4, 5

names = "Rock", "Paper", "Lizard", "Scissors", "Spock"


def conditions(a, b):
    return (a, b) in ((PAPER, ROCK), (SCISSORS, PAPER), (ROCK, SCISSORS),
                      (ROCK, LIZARD), (LIZARD, SPOCK), (SPOCK, SCISSORS),
                      (SCISSORS, LIZARD), (LIZARD, PAPER),
                      (PAPER, SPOCK), (SPOCK, ROCK))


print("""Please choose:
1: Rock
2: Paper
3: Lizard
4: Scissors
5: Spock""")


player = int(input("Choose from 1 to 5: "))
computer = choice((ROCK, PAPER, LIZARD, SCISSORS, SPOCK))

print(names[player-1], "vs", names[computer-1])

if computer != player:
    if conditions(player, computer):
        print("You win!")
    else:
        print("Better luck next time!")
else:
    print("It was a tie!")
