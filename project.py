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


    def determine_winner(self):
        ...


    def play_round(self):
        ...


    def get_player_choice(self):
        ...


    def display_rules(self):
        ...


def main():
    ...


if __name__ == '__main__':
    main()
