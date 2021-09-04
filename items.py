class Item:
    def __init__(self, name):
        self.name = name

    def is_equipment(self):
        pass


class Ingredient(Item):
    def __init__(self, name, code):
        super().__init__(name)
        self.code = code


# food, potions
class Consumable(Item):
    def __init__(self, name, restore):
        super().__init__(name)
        self.restore = restore

    def is_equipment(self):
        return False


class Equipment(Item):
    def __init__(self, name):
        super().__init__(name)

    def is_equipment(self):
        return True


class Weapon(Equipment):
    def __init__(self, name, weapon_type, base_damage, attacks):
        super().__init__(name)
        self.weapon_type = weapon_type
        self.base_damage = base_damage
        self.attacks = attacks


class Apparel(Equipment):
    def __init__(self, name, equip_slot, armor):
        super().__init__(name)
        self.equip_slot = equip_slot
        self.armor = armor
