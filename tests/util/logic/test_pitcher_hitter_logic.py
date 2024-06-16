"""Module for Test Player"""

from typing import List
import pytest
from hypothesis import given
from hypothesis.strategies import text, integers
from src.util.logic.pitcher_hitter_logic import PitcherHitterLogic
from src.util.generation import generate_player
from random import random


class TestPitcherHitterLogic:
    """Class for Player"""
        
    def test_quicklist_of_ints(self):
        rand_slug = int(random())
        ph_obj = PitcherHitterLogic(rand_slug)
        assert isinstance(ph_obj, PitcherHitterLogic)
        assert isinstance(ph_obj.rand_hit, float)
        assert isinstance(ph_obj.ump_odds, float)
        assert isinstance(ph_obj.hitability, float)

    