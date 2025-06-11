import random

def check(computer, user):
    if computer == user:
        return 0
    if (computer == 0 and user == 1):
        return -1
    if (computer == 1 and user == 2):
        return -1
    if (computer == 2 and user == 0):
        return -1
    return 1

# Get user input
user = int(input("Enter 0 for Snake, 1 for Water, and 2 for Gun: "))

# Generate computer choice
computer = random.randint(0, 2)

# Get the result
score = check(computer, user)

# Print choices
print("Computer chose:", computer)
print("You chose:", user)

# Print result
if score == 0:
    print("It's a Draw!")
elif score == -1:
    print("You Lose!")
else:
    print("You Win!")
