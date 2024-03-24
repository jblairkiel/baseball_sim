"""Module for Game Reults"""


class Game_Result:
    """Class for Game Result"""

    def __init__(self, team_a_runs: int, team_b_runs: int):
        if team_a_runs is None or team_b_runs is None:
            raise ValueError("Must have all attrs be not None")
        if team_a_runs <= 0 or team_b_runs <= 0:
            raise ValueError("Team runs must be positive")

        self.team_a_runs = team_a_runs
        self.team_b_runs = team_b_runs

        if self.team_a_runs > self.team_b_runs:
            self.winner = self.team_a_runs
            self.loser = self.team_b_runs
        else:
            self.winner = self.team_b_runs
            self.loser = self.team_a_runs
