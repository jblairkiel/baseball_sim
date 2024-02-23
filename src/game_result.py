class Game_Result():

    def __init__(self, teamA_runs: int, teamB_runs: int):

        self.teamA_runs = teamA_runs
        self.teamB_runs = teamB_runs
        
        if self.teamA_runs > self.teamB_runs:
            self.winner = self.teamA_runs
            self.loser = self.teamB_runs
        else:
            self.winner = self.teamB_runs
            self.loser = self.teamA_runs
  