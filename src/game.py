"""Module for game"""

import sys

sys.path.insert(0, "..")  # pragma: no mutate
from src.game_result import Game_Result
from src.team import Team


class Game:
    """Class for game"""

    def __init__(self, team_a: Team, team_b: Team, game_num: int = 1):

        self.team_a: Team = team_a
        self.team_b: Team = team_b
        self.game_num: int = game_num
        self.game_result: Game_Result
