from csv import reader


# read data from races.csv for codex
def read_race_data():
    race_data = {}

    with open('data/races.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            race_name = row[0].strip()
            race_data[race_name] = {
                'family': row[1].strip(),
                'attributes':
                    {
                        'strength': int(row[2].strip()),
                        'constitution': int(row[3].strip()),
                        'dexterity': int(row[4].strip()),
                        'speed': int(row[5].strip()),
                        'intelligence': int(row[6].strip())
                    },
                'loot_rates': {}
            }

            loot_rate_pairs = row[7].strip().replace('%', '').split('|')

            # interpret loot_rate pairs
            for pair in loot_rate_pairs:
                if pair == '':
                    continue
                percent, code = pair.split('.')
                race_data[race_name]['loot_rates'][code] = percent

    return race_data


# read data from races.csv for codex
def read_status_effects():
    status_effect_data = {}

    with open('data/status_effects.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            status_effect_data[row[0].strip()] = {
                'hp_drain': row[1].strip()}

    return status_effect_data


# map code to name from consumables.csv for codex
def read_ingredients_data():
    ingredients_data = {}

    with open('data/ingredients.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            ingredients_data[row[1].strip()] = {
                'name': row[0].strip()}

    return ingredients_data


# read data from consumables.csv for codex
def read_consumable_data():
    consumable_data = {}

    with open('data/consumables.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            consumable_data[row[0].strip()] = {
                'restore': row[1].strip()}

    return consumable_data


# read data from weapons.csv for codex
def read_weapon_data():
    weapon_data = {}

    with open('data/weapons.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            weapon_data[row[0].strip()] = {
                'weapon_type': row[1].strip(),
                'base_damage': row[2].strip()}

    return weapon_data


# read data from weapons.csv for codex
def read_attacks_data():
    attack_data = {}

    with open('data/attacks.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            attack_data[row[0].strip()] = {
                'aggressive': row[1].strip(),
                'defensive': row[2].strip(),
                'quick': row[3].strip(),
                'power': row[4].strip()
            }

    return attack_data


# read data from apparel.csv for codex
def read_apparel_data():
    apparel_data = {}

    with open('data/apparel.csv', 'r') as file:
        csv_reader = reader(file)
        # Skip header
        next(csv_reader)

        for row in csv_reader:
            apparel_data[row[0].strip()] = {
                'equip_slot': row[1].strip(),
                'armor': row[2].strip()}

    return apparel_data


# read txt files (All below this point)
def read_location_prefixes():
    prefixes = []
    with open('data/location_prefixes.txt', 'r') as file:
        for line in file.readlines():
            prefixes.append(line.replace('\n', ''))
    return prefixes


def read_location_suffixes():
    suffixes = []
    with open('data/location_suffixes.txt', 'r') as file:
        for line in file.readlines():
            suffixes.append(line.replace('\n', ''))
    return suffixes
