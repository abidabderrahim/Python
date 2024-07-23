import random

dice_r = {
    1: ("┌────────┐",
        "│        │",
        "│   ●    │",
        "│        │",
        "└────────┘"),
    2: ("┌────────┐",
        "│ ●      │",
        "│        │",
        "│      ● │",
        "└────────┘"),
    3: ("┌────────┐",
        "│ ●      │",
        "│   ●    │",
        "│     ●  │",
        "└────────┘"),
    4: ("┌────────┐",
        "│ ●    ● │",
        "│        │",
        "│ ●    ● │",
        "└────────┘"),
    5: ("┌────────┐",
        "│ ●    ● │",
        "│    ●   │",
        "│ ●    ● │",
        "└────────┘"),
    6: ("┌────────┐",
        "│ ●    ● │",
        "│ ●    ● │",
        "│ ●    ● │",
        "└────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("How Many Dice?: "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_r.get(dice[die]):
        print(line)

for die in dice:
    total += die

print(f"total: {total}")


