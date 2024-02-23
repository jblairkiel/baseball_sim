
from random import gauss
from src.team import Team
from src.game_result import Game_Result

class Game():

    def __init__(self, teamA: Team, teamB: Team, game_num=0,):

        self.avg_max_runs = 3
        self.avg_min_runs = 1
        self.teamA = teamA
        self.teamB = teamB
        self.game_num = game_num

    
    def simluate_game(self) -> Game_Result:

        #Dummy Logic Here

        teamA_runs = -1
        while teamA_runs < 0:
            teamA_runs =  self.teamA.value * gauss(self.avg_max_runs, self.avg_min_runs)

            
        teamB_runs = -1
        while teamB_runs < 0:
            teamB_runs =  self.teamB.value * gauss(self.avg_max_runs, self.avg_min_runs)

        gr = Game_Result(teamA_runs, teamB_runs)

        return gr
        