import random as rand
from random import gauss
from src.util.randoms import generate_random_name
from src.player import Player
from src.team import Team
from src.league import League
from src.game import Game
from src.util.logic.StrikeZone import StrikeZone
from typing import List, Dict



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


def generate_pitch() -> Dict:
    """Randomly generates a pitch within bounds"""
    pitch_choices = ["fb", "ch" "cur"]
   
    full_pitch_bounds = StrikeZone().get_full_bounds()

    # gaussian curve
    gaussian_x_mean = 0
    gaussian_y_mean = 0
    #gaussian_x_sigma = 1.15
    #gaussian_y_sigma = 1.2
    gaussian_x_sigma = full_pitch_bounds[0][0] / 2.25
    gaussian_y_sigma = full_pitch_bounds[1][0] / 2.25

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

    strike_pitch_bounds = StrikeZone().get_strike_bounds()
    x0_strike_bounds = strike_pitch_bounds[0][0]
    x1_strike_bounds = strike_pitch_bounds[0][1]
    y0_strike_bounds = strike_pitch_bounds[1][0]
    y1_strike_bounds = strike_pitch_bounds[1][1]
    # Implement Ump Error
    if (x0_strike_bounds < rand_x_pitch < x1_strike_bounds) and (
        y0_strike_bounds < rand_y_pitch < y1_strike_bounds
    ):
        outcome = "Strike"
    else:
        outcome = "Ball"

    return {
        "x": rand_x_pitch,
        "y": rand_y_pitch,
        "outcome": outcome,
        "pitch_type": rand_pitch_choice,
    }


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
