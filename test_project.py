import pytest
from project import Game
from io import StringIO


class TestGame:


    def test_valid_player_choice(self, monkeypatch):
        game = Game('Test Valid Player Choice', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        player_choice = game.get_player_choice()
        assert player_choice in game.choices


    def test_initial_player_score(self):
        game = Game('Test Player Score', 1)
        assert game.player.score == 0


    def test_round_number_increase(self, monkeypatch):
        game = Game('Test Round Number Increase', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        game.round_number = 0
        game.play_round()
        assert game.round_number == 1


    def test_invalid_player_choice(self, monkeypatch):
        game = Game('Test Invalid Player Choice', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        with pytest.raises(ValueError):
            game.get_player_choice('Invalid choice')


    def test_game_end(self, monkeypatch):
        game = Game('Test Game End', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        game.round_number = 3
        assert game.round_number == game.num_rounds


    def test_display_player_choice(self, monkeypatch):
        game = Game('Test Display Player Choice', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        assert game.get_player_choice('Enter your choice (1-6): ') == game.choices[0]


    def test_valid_computer_choice(self):
        game = Game('Test Valid Computer choice', 1)
        computer_choice = game.computer_choice()
        assert computer_choice in game.choices


    def test_invalid_computer_choice(self):
        ...
