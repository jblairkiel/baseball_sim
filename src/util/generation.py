import random as rand
from random import gauss
from src.game_result import Game_Result
from src.util.randoms import generate_random_name
from src.player import Player
from src.team import Team
from src.pitch import Pitch
from src.league import League
from src.game import Game
from src.util.logic.StrikeZone import StrikeZone
from typing import List, Dict

#TODO beef up
def generate_game():
    team_a = generate_team()
    team_b = generate_team()
    game_obj = Game(team_a, team_b)
    return game_obj

def generate_game_result():
    team_a_runs = int(gauss(4, 2))
    team_b_runs = int(gauss(4, 2))
    game_obj = Game_Result(team_a_runs, team_b_runs)
    return game_obj

def simluate_game(self, team_a: Team, team_b: Team) -> Game_Result:
        """Simulates a game"""
        # Dummy Logic Here

        team_a_runs = int(self.team_a.value * gauss(
            self.avg_max_runs, self.avg_min_runs
        ))

        team_b_runs = int(self.team_b.value * gauss(
            self.avg_max_runs, self.avg_min_runs
        ))

        if team_a_runs == team_b_runs:
            # Eventually sim more innings
            walkoff_chance = rand.randrange(1,2)
            gr = Game_Result(team_a_runs + 1, team_b_runs) if walkoff_chance % 2 == 0 else Game_Result(team_a_runs, team_b_runs + 1)
            return gr
        else:
            return Game_Result(team_a_runs 1, team_b_runs) 

        return gr

def generate_player(position, jersey_num=None) -> Player:
    """Randomy Generates a player"""
    f_name, l_name = generate_random_name()

    # Generate a random character class and race for the new player
    new_player = Player(position, jersey_num, f_name, l_name)
    return new_player


def generate_team() -> Team:
    """Randomly generates a team"""
    # Rostered team
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    team_roster = []
    for i, _ in enumerate(position_list):
        new_player = generate_player(position_list[i])
        team_roster.append(new_player)

    # Coach
    coach_f_name, coach_l_name = generate_random_name()

    # Testing functions within utils/random_names.py
    # assert isinstance(generate_random_name(), tuple), 'Function `generate_random_name()` did not return a tuple.'

    teamname = f"Team #{rand.randrange(0,100)}"

    # Team Value
    team_value = rand.randrange(0, 20)
    return Team(
        teamname,
        players=team_roster,
        coach=f"{coach_f_name} {coach_l_name}",
        team_value=team_value,
    )


def generate_league() -> League:
    """Randomly generates a league"""
    # League Size
    league_size = 30
    league_list = []
    for _ in range(1, league_size):
        new_team = generate_team()
        league_list.append(new_team)

    # Testing functions within utils/random_names.py
    # assert isinstance(generate_random_name(), tuple), 'Function `generat

    for a in league_list:
        print(a)


def generate_pitch() -> Pitch:
    """Randomly generates a pitch within bounds"""
    pitch_choices = ["fb", "ch" "cur"]
   
    full_pitch_bounds = StrikeZone().get_full_bounds()

    # gaussian curve
    gaussian_x_mean = 0
    gaussian_y_mean = 0
    #gaussian_x_sigma = 1.15
    #gaussian_y_sigma = 1.2
    gaussian_x_sigma = full_pitch_bounds[0][0] / 2.55
    gaussian_y_sigma = full_pitch_bounds[1][0] / 2.55

    try:
        rand_x_pitch = gauss(gaussian_x_mean, gaussian_x_sigma)
    except Exception as _:
        print("Invalid X Bounds")
        return None
    try:
        rand_y_pitch = gauss(gaussian_y_mean, gaussian_y_sigma)
    except Exception as _:
        print("Invalid Y Bounds")
        return None
    rand_pitch_choice = rand.choice(pitch_choices)
    pitch = Pitch(rand_x_pitch, rand_y_pitch, rand_pitch_choice)

    return pitch




def generate_game_runs(team_a: Team, team_b: Team) -> List[int]:
    """Randomly Generates Game Results"""
    # Dummy Logic Here

    team_a_runs = -1
    while team_a_runs < 0:
        team_a_runs = team_a.value * gauss(3, 1)

    team_b_runs = -1
    while team_b_runs < 0:
        team_b_runs = team_b.value * gauss(3, 1)

    return [team_a_runs, team_b_runs]


if __name__ == "__main__":
    print("Running generation module")
