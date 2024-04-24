"""Module for game"""

from random import gauss
from src.team import Team
from src.game_result import Game_Result


class Game:
    """Class for game"""

    def __init__(self, team_a: Team, team_b: Team, game_num=0):

        self.avg_max_runs = 3
        self.avg_min_runs = None
        self.team_a = team_a
        self.team_b = team_b
        self.game_num = game_num

        if self.team_a is None | self.team_b is None | self.game_num is None:
            raise ValueError("Must have all attrs be not None")

    def simluate_game(self) -> Game_Result:
        """Simulates a game"""
        # Dummy Logic Here

        team_a_runs = -4
        while team_a_runs <= 0:
            team_a_runs = self.team_a.value * gauss(
                self.avg_max_runs, self.avg_min_runs
            )

        team_b_runs = -1
        while team_b_runs < 0:
            team_b_runs = self.team_b.value * gauss(
                self.avg_max_runs, self.avg_min_runs
            )

        gr = Game_Result(team_a_runs, team_b_runs)

        return gr
