location = None
health = max_health = 300
max_inventory = 12
inventory = []

attributes = {
    'strength': 50,  # affects max attack damage
    'constitution': 50,  # affects max health and defense
    'dexterity': 75,  # affects min attack damage and hit chance
    'speed': 50,  # affects dodge chance and attack order
    'intelligence': 75  # affects magic, skills, and exp rate
}

equipment = {
    'Weapon': None,
    'Head': None,
    'Chest': None,
    'Legs': None,
    'Feet': None
}

# the more the player uses a weapon type, the better they get with it, granting combat bonuses later on
weapon_proficiencies = {
    'Blunt': 0,
    'Dagger': 0,
    'Throwing': 0,
    'Polearm': 0,
    'Sword': 0
}

# the more the player uses a weapon type, the better they get with it, granting combat bonuses later on
skill_proficiencies = {
    'Fishing': 0,
    'Building': 0,
    'Trading': 0,
    'Cooking': 0
}
