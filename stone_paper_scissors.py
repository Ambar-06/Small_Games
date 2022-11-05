import random as rp

def main():
    user_input()

def user_input():
    choose = input("Please choose an option: Stone, Paper, or Scissor: ")
    options = ["stone", "paper", "scissor"]
    computer = rp.choice(options)

    if choose.lower() == computer:
        print(f"It's a draw!")

    elif computer == "stone":
        if choose.lower() == "scissor":
            print(f"Computer won!")
        else:
            print(f"You won!")

    elif computer == "paper":
        if choose.lower() == "stone":
            print(f"Computer won!")
        else:
            print(f"You won!")

    elif computer == "scissor":
        if choose.lower() == "paper":
            print(f"Computer won!")
        else:
            print(f"You won!")
            
    print(f"The computer chose {computer.capitalize()}")


if __name__ == "__main__":
    main()