import random

# Dice face art using ASCII
Dice_art = {
    1: (
        "┌─────────┐",
        "|         |",
        "|    ●    |",
        "|         |",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "| ●       |",
        "|         |",
        "|       ● |",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "| ●       |",
        "|    ●    |",
        "|       ● |",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "| ●     ● |",
        "|         |",
        "| ●     ● |",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "| ●     ● |",
        "|    ●    |",
        "| ●     ● |",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "| ●     ● |",
        "| ●     ● |",
        "| ●     ● |",
        "└─────────┘"
    )
}

# Ask user how many dice
number_of_dice = int(input("How many dice? : "))

# Roll the dice
dice = [random.randint(1, 6) for _ in range(number_of_dice)]
total = sum(dice)

# Print the dice numbers
print("You rolled:", dice)

# Print dice art side by side
for line in range(5):  # Each die art has 5 lines
    print("   ".join(Dice_art[d][line] for d in dice))

# Print total
print(f"Total: {total}")
