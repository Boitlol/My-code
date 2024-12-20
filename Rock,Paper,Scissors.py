import random
ascii_art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

print("Welcome to Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]

user_choice = input("Type 'rock', 'paper', or 'scissors': ").lower()
if user_choice not in choices:
    print("Invalid choice. Please restart and type 'rock', 'paper', or 'scissors'.")
else:
    computer_choice = random.choice(choices)

    print("You chose:")
    print(ascii_art[user_choice])
    print("Computer chose:")
    print(ascii_art[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
