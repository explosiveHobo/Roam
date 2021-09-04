import random
import player_model


def get_location():
    return player_model.location


def add_item(item):
    if player_model.inventory.__len__() < player_model.max_inventory:
        player_model.inventory.append(item)


def print_inventory():
    for item in player_model.inventory:
        print('\t' + item.name)


# noinspection PyUnresolvedReferences
def survey():
    print('\nYou are currently at ' + player_model.location.name)

    for direction, vector in player_model.location.vectors.items():
        print('\t' + vector.locations[1].name + ' is ' + str(vector.distance) + ' units ' + direction)
    print('\n')


# move to a new location depending on direction, returns false on combat encounter and true on safe travel
def move(command):
    direction = command.split(' ')[1]
    vector = player_model.location.vectors[direction]
    player_model.location = vector.locations[1]

    # check rudimentary guess for combat encounter, and ?stop in between locations if combat
    if random.randint(1, 6) < vector.distance:
        return False

    return True
