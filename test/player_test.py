import pytest
from src.player import Player
from src.util.generation import generate_player

class Player_Test:

    def test_single_player_generate():
        x = generate_player()
        assert type(x) == Player
