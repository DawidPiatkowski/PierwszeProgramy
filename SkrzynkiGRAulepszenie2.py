import random

def get_box_color():
    rand_num = random.random()
    if rand_num <= 0.75:
        return "green"
    elif rand_num <= 0.95:
        return "orange"
    elif rand_num <= 0.99:
        return "purple"
    else:
        return "gold"

def open_box(color):
    if color == "green":
        return 1000
    elif color == "orange":
        return 4000
    elif color == "purple":
        return 9000
    elif color == "gold":
        return 16000
    else:
        return 0

def main():
    print("Welcome to the Room Adventure!")
    total_gold = 0
    
    for move in range(1, 6):
        print(f"\nMove {move}: You're moving through the room...")
        
        roll = random.random()
        if roll <= 0.4:
            print("You found nothing this time.")
        else:
            box_color = get_box_color()
            print(f"You found a {box_color} box!")
            gold_found = open_box(box_color)
            total_gold += gold_found
            print(f"Congratulations! You found {gold_found} gold.")

    print("\nGame Over")
    print(f"Total gold collected: {total_gold}")

if __name__ == "__main__":
    main()
