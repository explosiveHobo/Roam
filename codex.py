import pipeline

# name of race maps to {family, attributes . . .}
RACE_DATA = {}

# status effect name maps to effect
STATUS_EFFECTS_DATA = {}

# name of ingredient maps to code
INGREDIENTS_DATA = {}

# name of consumable maps to health restore amount
CONSUMABLE_DATA = {}

# name of weapon maps to {weapon_type,base_damage}
WEAPON_DATA = {}

# weapon type maps to move names
ATTACKS_DATA = {}

# name of apparel maps to {equip_slot,armor}
APPAREL_DATA = {}

LOCATION_SUFFIXES = []
LOCATION_PREFIXES = []


def initialize():
    global RACE_DATA
    global STATUS_EFFECTS_DATA
    global INGREDIENTS_DATA
    global CONSUMABLE_DATA
    global WEAPON_DATA
    global ATTACKS_DATA
    global APPAREL_DATA
    global LOCATION_PREFIXES
    global LOCATION_SUFFIXES

    RACE_DATA = pipeline.read_race_data()
    STATUS_EFFECTS_DATA = pipeline.read_status_effects()
    INGREDIENTS_DATA = pipeline.read_ingredients_data()
    CONSUMABLE_DATA = pipeline.read_consumable_data()
    WEAPON_DATA = pipeline.read_weapon_data()
    ATTACKS_DATA = pipeline.read_attacks_data()
    APPAREL_DATA = pipeline.read_apparel_data()

    LOCATION_PREFIXES = pipeline.read_location_prefixes()
    LOCATION_SUFFIXES = pipeline.read_location_suffixes()
