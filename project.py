import random


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Game:
    def __init__(self, player_name, num_rounds):
        self.choices = ["rock", "paper", "scissors", "lizard", "spock"]
        self.player = Player(player_name)
        self.computer = Player("Computer")
        self.num_rounds = num_rounds
        self.round_number = 0

    def determine_winner(self, player_choice, computer_choice):
        rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"],
        }

        if player_choice == computer_choice:
            return f"{Colors.YELLOW}Draw!{Colors.RESET}"
        elif computer_choice in rules[player_choice]:
            self.player.score += 1
            return f"{Colors.RED}You score!{Colors.RESET}"
        else:
            self.computer.score += 1
            return f"{Colors.BLUE}Computer scores!{Colors.RESET}"

    def determine_final_winner(self):
        if self.player.score > self.computer.score:
            return f"{Colors.RED}You are the champion!{Colors.RESET}"
        elif self.player.score < self.computer.score:
            return f"{Colors.BLUE}Computer is the champion!{Colors.RESET}"
        else:
            return f"{Colors.YELLOW}Draw?!{Colors.RESET}"

    def play_round(self):
        player_choice = self.get_player_choice()
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)

        self.round_number += 1
        return f"""{Colors.RED}You chose: {player_choice}{Colors.RESET}\n{Colors.BLUE}Computer chose: {computer_choice}{Colors.RESET}
{Colors.RED}Your score: {self.player.score}{Colors.RESET}, {Colors.BLUE}Computer score: {self.computer.score}{Colors.RESET}
{result}
"""

    def get_player_choice(self):
        while True:
            print(f"\n{Colors.RED}Choose your move!{Colors.RESET}\n")
            for i, choice in enumerate(self.choices, start=1):
                print(f"{i}. {choice}")
            print(f"0. Quit\n6. Read rules\n")
            choice_index = input("Enter your choice (1-6): ")

            if choice_index == "0":
                print(f"\n{Colors.GREEN}Thanks for playing!{Colors.RESET}")
                exit()

            if choice_index == "6":
                self.display_rules()
                continue

            try:
                if choice_index.isdigit() and 1 <= int(choice_index) <= 5:
                    return self.choices[int(choice_index) - 1]
                elif choice_index == "":
                    return random.choice(self.choices)
            except Exception as e:
                print(f"Invalid choice: {e}. Please choose a number between 1 and 6")

    def display_rules(self):
        rules = """Scissors cuts paper,
Paper covers rock,
Rock crushes lizard,
Lizard poisons Spock,
Spock smashes scissors,
Scissors decapitates lizard,
Lizard eats paper,
Paper disproves Spock,
Spock vaporizes rock,
and as it always has,
Rock crushes scissors."""
        print(f"\nRules of the Game: {rules}")


def main():
    player_name = str(input("User?! Please enter your name: ").strip())
    if player_name == "":
        player_name = "User"
    num_rounds = input(
        f"Welcome {Colors.RED}{player_name}{Colors.RESET}!\nPlease enter the amount of rounds you want to play: "
    )
    if num_rounds == "":
        num_rounds = 3
        print(f"Default round number: {num_rounds}")
    game = Game(player_name, int(num_rounds))
    while game.round_number < game.num_rounds:
        print(game.play_round())
    print(game.determine_final_winner())


if __name__ == "__main__":
    main()
