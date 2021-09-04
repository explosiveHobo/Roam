class Creature:
    def __init__(self, race):
        self.race = race  # Unique race label
        self.family = None  # Ascendant, Beast, Undead (Race 'Groups')
        self.attributes = {
            'strength': -1,  # affects max attack damage
            'constitution': -1,  # affects max health and defense
            'dexterity': -1,  # affects min attack damage and hit chance
            'speed': -1,  # affects dodge chance and attack order
            'intelligence': -1  # affects magic, skills, and exp rate
        }

        # integer to be less than maps to loot item, in ascending numeric order
        self.loot_rates = {}
        # self.loot_rates = {15: '15%loot',
        #                   50: '35%loot',
        #                   100: '50%loot'}

        self.health = self.max_health = -1

    def calculate_stats(self):
        self.max_health = (self.attributes['constitution'] * 5) + self.attributes['strength']
