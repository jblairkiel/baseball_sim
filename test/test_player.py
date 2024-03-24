import pytest
from hypothesis import given    
from hypothesis.strategies import text, integers
from src.player import Player
from src.util.generation import generate_player

class TestPlayer():

    # def test_single_player_generate():
    #     x = generate_player()
    #     assert type(x) == Player


    @given(text(), text(), integers(1,9), integers(0,99))
    def test_generate_single_random_player(self, f, l, p, n):
        '''Tests if a single player can be created'''
        lst = []
        magic_num = 10000
        for _ in range(0, magic_num):
            new_player = Player(p, n ,f, l)

            lst.append(new_player)
        for a in range(0, 10):
            print(lst[a])
        
        assert len(lst) == magic_num

