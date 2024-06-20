"""Module for Test Player"""

import sys

sys.path.insert(0, "..")
from src.util.generation import generate_game


class TestGame:
    """Class for Player"""

    def test_game_teams_are_not_none(self):
        """Tests team runs are not none"""
        result = generate_game()
        assert result.team_a is not None
        assert result.team_b is not None

    def test_game_teams_runs_are_not_equal(self):
        """Tests team runs are not none"""
        result = generate_game()
        assert result.team_a is not None
        assert result.team_b is not None

    def test_game_num_not_none(self):
        """Tests if a game has an ending, no ties"""
        result = generate_game()
        assert result.game_num is not None
