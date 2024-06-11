"""Module for Test Team"""

import pytest
from hypothesis import given
from hypothesis.strategies import text, integers
from src.team import Team
from src.util.generation import generate_team


class TestTeam:
    """Class for Team"""

    # def test_single_team_generate():
    #     x = generate_team()
    #     assert type(x) == Team

    def test_generate_team_is_not_none(self):
        """Tests if Nones are passed in"""
        new_team = generate_team()
        new_team is not None

    # @given(text(), text(), integers(1,9), integers(0,99))
    def test_generate_single_random_team(self):
        """Tests if a single team can be created"""
        lst = []
        magic_num = 10
        for _ in range(0, magic_num):
            new_team = generate_team()

            lst.append(new_team)
        for a in range(0, 10):
            print(lst[a])

        assert len(lst) == magic_num

    def test_team_creation_none(self):
        """Tests if Nones are passed in"""
        try:
            new_team = Team(None, None, None, None)
            if new_team is None:
                assert False
        except ValueError as _:
            assert True

    # def test_team_creation_can_(self):
    #     '''Tests if Nones are passed in'''
    #     try:
    #         new_team = Team(None, None, None, None)
    #         if new_team is None:
    #             assert False
    #     except ValueError as _:
    #         assert True
