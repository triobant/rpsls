import random


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0


class Game():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.player_name = Player(player_name)
        self.computer_name = Player('computer')
        self.num_rounds = num_rounds
        self.round_number = round_number


    def determine_winner(self, player_choice, computer_choice):
        rules = {
                'rock': ['scissors', 'lizard'],
                'paper': ['rock', 'spock'],
                'scissors': ['paper', 'lizard'],
                'lizard': ['paper', 'spock'],
                'spock': ['rock', 'scissors']
        }
        if player_choice == computer_choice:
            return 'Draw!', 0
        elif computer_choice in rules[player_choice]:
            return 'You win!'
        else:
            return 'Computer wins!'


    def play_round(self):
        ...


    def get_player_choice(self):
        ...


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
        print(f'\nRules of the Game: {rules}')


def main():
    ...


if __name__ == '__main__':
    main()
