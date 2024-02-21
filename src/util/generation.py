import random as rand
from random import gauss
from src.util.randoms import generate_random_name
from src.player import Player
from src.team import Team

def generate_player(position, jersey_num=None):
    
    f_name, l_name = generate_random_name()


    # Generate a random character class and race for the new player
    new_player = Player(f_name, l_name, position, jersey_number=jersey_num)
    return new_player

def generate_team():
    #Rostered team
    posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    teamRoster = []
    for i in range(0, len(posList)):
        new_player = generate_player(posList[i])
        teamRoster.append(new_player)


    #Coach
    coach_f_name, coach_l_name = generate_random_name()

    # Testing functions within utils/random_names.py
    #assert isinstance(generate_random_name(), tuple), 'Function `generate_random_name()` did not return a tuple.'   

    teamname = f"Team #{rand.randrange(0,100)}"
    return Team(teamname, players=teamRoster, coach=f"{coach_f_name} {coach_l_name}")
    
def generate_league():
    #League Size
    league_size = 30
    league_list = []
    for i in range(1, league_size):
        new_team = generate_team()
        league_list.append(new_team)



    # Testing functions within utils/random_names.py
    #assert isinstance(generate_random_name(), tuple), 'Function `generat
        
    [print(a) for a in league_list]
    
def generate_pitch():

    x0_full_bounds = -2.0
    x1_full_bounds = 2.0
    y0_full_bounds = -2.0
    y1_full_bounds = 2.0

    x0_strike_bounds = -1.0
    x1_strike_bounds = 1.0
    y0_strike_bounds = -1.0
    y1_strike_bounds = 1.0
    #gaussian curve 

    gaussian_x_mean = 0
    gaussian_y_mean = 0
    gaussian_x_sigma = 1.15
    gaussian_y_sigma = 1.2


    rand_x_pitch = gauss(gaussian_x_mean, gaussian_x_sigma)
    rand_y_pitch = gauss(gaussian_y_mean, gaussian_y_sigma)

    #Implement Ump Error
    if (x0_strike_bounds < rand_x_pitch < x1_strike_bounds) and (y0_strike_bounds < rand_y_pitch < y1_strike_bounds):
        outcome = "Strike"
    else:
        outcome = "Ball"

    return {
        "x": rand_x_pitch,
        "y": rand_y_pitch,
        "outcome" : outcome
    }