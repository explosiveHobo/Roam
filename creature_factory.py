from random import randrange, choice
import creatures
import codex


# return a random race string that is a member of a certain family
def random_race_from_family(family):
    all_race_data = codex.RACE_DATA
    matching_races = []

    for race, data in all_race_data.items():
        if data['family'] == family:
            matching_races.append(race)

    return choice(matching_races)


# create a creature object and populate its fields, then return it
def create_creature_from_race(race, percent_deviation=0):
    # pull relevant race data from codex
    race_data = codex.RACE_DATA[race]

    # create the creature
    creature = creatures.Creature(race)

    # absolute attributes
    if percent_deviation == 0:
        creature.attributes = race_data['attributes']
    # deviated attributes
    else:
        for attribute_name, base_value in race_data['attributes'].items():
            numeric_deviation = int(base_value * (percent_deviation / 100))
            creature.attributes[attribute_name] = base_value + randrange(-numeric_deviation, numeric_deviation)

    creature.loot_rates = race_data['loot_rates']

    creature.calculate_stats()
    creature.health = creature.max_health

    return creature


# pass a creature object to fill its fields based on race
# attribute deviation (percentage) randomizes attributes by percent_deviation from base value
def define_creature_from_race(creature, percent_deviation=0):
    # pull relevant race data from codex
    race_data = codex.RACE_DATA[creature.race]

    # absolute attributes
    if percent_deviation == 0:
        creature.attributes = race_data['attributes']
    # deviated attributes
    else:
        for attribute_name, base_value in race_data['attributes']:
            numeric_deviation = int(base_value * (percent_deviation / 100))
            creature.attributes[attribute_name] = base_value + randrange(-numeric_deviation, numeric_deviation)

    creature.calculate_stats()
    creature.health = creature.max_health
