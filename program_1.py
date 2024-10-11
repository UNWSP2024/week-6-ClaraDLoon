#Program #1: Random Dice
#Clara Riley
#Luke Snell
#10/11/24

import random


def randDice():
    # Simulate rolling two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def main():
    total = 0
    rolls = 100

    for _ in range(rolls):
        total += randDice()

    average = total / rolls
    print(f"Average of 100 rolls: {average:.2f}")


if __name__ == "__main__":
    main()
