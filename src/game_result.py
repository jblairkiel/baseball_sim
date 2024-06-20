"""Module for Game Reults"""

from src.team import Team


class Game_Result:
    """Class for Game Result"""

    def __init__(self, team_a: Team, team_b: Team, team_a_runs: int, team_b_runs: int):

        self.team_a_runs = team_a_runs
        self.team_b_runs = team_b_runs

        if self.team_a_runs > self.team_b_runs:
            self.winner = self.team_a_runs
            team_a.record_win()
            self.loser = self.team_b_runs
            team_b.record_loss()
        else:
            self.winner = self.team_b_runs
            team_b.record_win()
            self.loser = self.team_a_runs
            team_a.record_loss()
