import random as rand

import names
import plotly.express as px

from src.enums.misc_enums import Genders

# def generate_number_names():
#     # rand.seed(1) # Use a fixed seed so we always get the same numbers when testing

#     first_names = quicklist_of_ints(0, 9)
#     last_names = quicklist_of_ints(44, 53)
#     rand.shuffle(number_names)

#     posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_random_name():
    first_name = names.get_first_name(gender=Genders.MALE)
    last_name = names.get_last_name()

    return first_name, last_name


def quicklist_of_ints(start: int, ending: int):

    strlist = []
    for i in range(1, ending):
        strlist.append(str(i))

    return strlist


def generate_random_number(numrange: int):

    return rand.randrange(0, numrange)


def generate_random_df():
    df = px.data.iris()  # iris is a pandas DataFrame
    return df


# def generate_random_pitch_df():
#     pitch_dict = []
#     pitch_hitability_dict = []

#     player_dict = []
#     player_hitability_dict = []
#     for i in range(0, 1000):
#         pos_choice = i % 9
#         player = generate_player(pos_choice)
#         pitch = generate_pitch()
#         at_bat_pitch = get_pitch_at_atbat(player, pitch)
#         at_bat_pitch = at_bat_pitch.__dict__
#         player_hitability_dict.append(at_bat_pitch)

#     df = pd.DataFrame(player_hitability_dict)
