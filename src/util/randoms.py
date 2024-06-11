import random as rand
import names

# def generate_number_names():
#     # rand.seed(1) # Use a fixed seed so we always get the same numbers when testing

#     first_names = quicklist_of_ints(0, 9)
#     last_names = quicklist_of_ints(44, 53)
#     rand.shuffle(number_names)

#     posList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_random_name():
    first_name = names.get_first_name(gender="male")
    last_name = names.get_last_name()

    return first_name, last_name


def quicklist_of_ints(start, ending):

    strlist = []
    for i in range(1, ending):
        strlist.append(str(i))

    return strlist


def generate_random_number(numrange):

    return rand.randrange(0, numrange)
