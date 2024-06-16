"""Module for Test Player"""

from typing import List
import pytest
from hypothesis import given
from hypothesis.strategies import text, integers
from src.util.randoms import generate_random_name, generate_random_number, quicklist_of_ints
from src.util.generation import generate_player
from random import randint


class TestRandom:
    """Class for Player"""

    # def test_single_player_generate():
    #     x = generate_player()
    #     assert type(x) == Player

    def test_generate_random_name(self):
        first, last = generate_random_name()
        assert isinstance(first, str)
        assert isinstance(last, str)
        
    def test_quicklist_of_ints(self):
        end = randint(0, 100)
        lst_str = quicklist_of_ints(1, end)
        assert isinstance(lst_str, List)

    def test_generate_random_number(self):
        end = randint(0, 100)
        ran_int = generate_random_number(end)
        assert isinstance(ran_int, int)
    