import pytest
from project import Game
from io import StringIO


class TestGame:


    def test_valid_player_choice(self, monkeypatch):
        game = Game('Player', 1)
        monkeypatch.setattr('sys.stdin', StringIO('1\n'))
        player_choice = game.get_player_choice()
        assert player_choice in game.choices


    def test_initial_player_score(self):
        ...


    def test_round_number_increase(self, monkeypatch):
        ...


    def test_invalid_player_choice(self, monkeypatch):
        ...


    def test_game_end(self, monkeypatch):
        ...


    def test_display_player_choice(self, monkeypatch):
        ...


    def test_valid_computer_choice(self):
        ...


    def test_invalid_computer_choice(self):
        ...
