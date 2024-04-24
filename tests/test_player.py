"""Module for Test Player"""

import pytest
from hypothesis import given
from hypothesis.strategies import text, integers
from src.player import Player
from src.util.generation import generate_player


class TestPlayer:
    """Class for Player"""

    # def test_single_player_generate():
    #     x = generate_player()
    #     assert type(x) == Player
    def test_player_attrs_not_none():
        player_obj = generate_player()
        assert player_obj.first_name is not None
        assert player_obj.last_name is not None
        assert player_obj.position is not None
        assert player_obj.stats is not None

    def test_player_str_not_none():
        player_obj = generate_player()
        assert player_obj.__str__() is not None

    @given(text(), text(), integers(1, 9), integers(0, 99))
    def test_generate_single_random_player_random_chars(self, f, l, p, n):
        """Tests if a single player can be created"""
        lst = []
        magic_num = 10000
        for _ in range(0, magic_num):
            new_player = Player(p, n, f, l)

            lst.append(new_player)
        for a in range(0, 10):
            print(lst[a])

        assert len(lst) == magic_num

    def test_generate_multiple_random_player_generator(self):
        """Tests if a single player can be created"""
        lst = []
        magic_num = 100
        for _ in range(0, magic_num):
            for player_num in range(1, 9):
                new_player = generate_player(player_num)
                lst.append(new_player)
                print(new_player)

        assert len(lst) == magic_num * 8

    def test_player_creation_none(self):
        """Tests if Nones are passed in"""
        try:
            new_player = Player(None, None, None, None)
            if new_player is None:
                assert False
        except ValueError as _:
            assert True

    @given(text(), text(), integers(1, 9), integers(0, 99))
    def test_player_creation_none_stats(self, f, l, p, n):
        """Tests if a single player can be created"""
        new_player = Player(p, n, f, l)
        if new_player.stats is None:
            assert False
        else:
            assert True
