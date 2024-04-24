"""Module for Test Player"""

import sys
from hypothesis import given
from hypothesis.strategies import text, integers
sys.path.insert(0, "..")
from src.player import Player
from src.util.generation import generate_game_result


class TestGameResult:
    """Class for Player"""

    def test_teams_are_not_none(sel ):
        """Tests team runs are not none"""
        result = generate_game_result()
        assert result.team_a_runs is not None
        assert result.team_b_runs is not None

    def test_always_a_winner(self):
        """Tests if a game has an ending, no ties"""
        result = generate_game_result()
        assert result.team_a_runs != result.team_b_runs

    def test_always_winner_lower(self):
        """Tests if a game has an ending, always winner loser"""
        result = generate_game_result()
        assert result.winner is not None
        assert result.loser is not None

    @given(text(), text(), integers(1, 9), integers(0, 99))
    def test_player_creation_none_stats(self, f, l, p, n):
        """Tests if a single player can be created"""
        new_player = Player(p, n, f, l)
        if new_player.stats is None:
            assert False
        else:
            assert True
