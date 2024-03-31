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
        self.round_number = 0


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
            return 'You win!', 1
        else:
            return 'Computer wins!', -1


    def play_round(self):
        ...


    def get_player_choice(self):
        while True:
            print('Choose your move: ')
            for i, choice in enumerate(self.choices, start=1):
                print(f'{i}. {choice}')
            print('0. Quit')
            print('7. Read rules')
            choice_index = input("Enter your choice (0-7): ")

            if choice_index == '0':
                print('Thanks for playing!')
                exit()

            if choice_index == '7':
                self.display_rules()
                continue

            if choice_index.isdigit() and 0 <= int(choice_index) <= 5:
                return self.choices[int(choice_index)]
            else:
                print('Invalid choice. Please choose a number between 0 and 7')


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
    player_name = input('Player! Please enter your name: ')
    num_rounds = int(input(f'Welcome {player_name}! Please enter the amount of rounds you want to play: '))
    game = Game(player_name, num_rounds)
    while game.round_number < game.num_rounds:
        game.play_round()


if __name__ == '__main__':
    main()
