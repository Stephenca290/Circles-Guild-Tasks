import random

def roll_dice():
    """Return a random integer between 1 and 6 inclusive."""
    return random.randint(1, 6)

def main():
    print("\n🎲 Welcome to the Dice Simulator! 🎲\n")
    while True:
        user_choice = input("Roll the dice? (y/n): ").strip().lower()
        if user_choice == "y":
            result = roll_dice()
            print(f"✅ You rolled: {result}\n")
        elif user_choice == "n":
            print("👋 Thanks for playing! Goodbye.")
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
