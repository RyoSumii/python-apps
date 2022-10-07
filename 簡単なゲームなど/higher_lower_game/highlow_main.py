from game_data import data
from highlow_art import logo, vs
import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def random_num():
    n = random.randint(0, 50)
    return n


def check(dict_a, dict_b):
    count1 = dict_a['follower_count']
    count2 = dict_b['follower_count']
    if count1 > count2:
        return 'A'
    else:
        return 'B'


def return_count(dictionary):
    count = dictionary['follower_count']
    return count


def show_dict_compare(dictionary):
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']
    print(f"Compare A: {name}, {description}, from {country}.")


def show_dict_against(dictionary):
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']
    print(f"Against B: {name}, {description}, from {country}.")


def game_format(a_dict, b_dict):
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    show_dict_compare(a_dict)
    print(vs)
    show_dict_against(b_dict)


a_num = random_num()
while True:
    b_num = random_num()
    if b_num == a_num:
        b_num = random_num()
    else:
        break

compare = data[a_num]
against = data[b_num]

score = 0
while True:

    # return greater count dict
    result = check(compare, against)

    game_format(compare, against)
    # if score > 0:
    #   print(f"You're right! Current score: {score}")

    answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()

    if answer == result:
        score += 1
        clearConsole()
        compare = against
        while True:
            num = random_num()
            against = data[num]
            if compare == against:
                continue
            else:
                break

    else:
        clearConsole()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
