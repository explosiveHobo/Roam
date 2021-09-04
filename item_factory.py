from items import Weapon, Apparel, Ingredient
import codex


def create_ingredient(code):
    return Ingredient(codex.INGREDIENTS_DATA[code]['name'], code)


def create_weapon(name):
    data = codex.WEAPON_DATA[name]
    # attacks is a dict
    attacks = codex.ATTACKS_DATA[data['weapon_type']]
    return Weapon(name, data['weapon_type'], int(data['base_damage']), attacks)


def create_apparel(name):
    data = codex.APPAREL_DATA[name]
    return Apparel(name, data['equip_slot'], int(data['armor']))
