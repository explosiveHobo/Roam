import codex
import player_mediator
import player_model
import item_factory as itf
import creature_factory as cf
from random import randint
from time import sleep

# can affect things all throughout the battle. Think field buff/debuff
battle_modifier = 'New Battle'


# returns true on successful flee
def try_flee(monster):
    print('You attempt to flee...\n')
    sleep(.75)
    # flee with superior speed
    if player_model.attributes['speed'] > monster.attributes['speed']:
        print('\tSuccessfully fled the battle.\n')
        return True
    # flee with previous move as defensive plus luck, or just luck
    elif battle_modifier == 'Improved Flee Chance' and randint(0, 2) == 1 or randint(0, 5) == 1:
        print('Successfully fled the battle.\n')
        return True
    print('\tbut could not escape.\n')
    sleep(.75)
    return False


# guide the user through choosing an attack, then apply that damage to the enemy returning debuff
def attack_prompt(monster):
    global battle_modifier

    # get relevant attributes
    dex = player_model.attributes['dexterity']
    m_dex = monster.attributes['dexterity']
    spd = player_model.attributes['speed']
    m_spd = monster.attributes['speed']
    strength = player_model.attributes['strength']
    m_strength = monster.attributes['strength']

    damage = 0
    dodge_chance = 0  # calculations may need tweaking
    hit_chance = 0  # calculations may need tweaking

    weapon = player_model.equipment['Weapon']
    attacks = list((weapon.attacks.values()))
    debuff = None

    # unused
    proficiency = (player_model.weapon_proficiencies[weapon.weapon_type])

    print('\nWhich attack will you use? (1: aggressive, 2: defensive, 3: quick, 4: power, 5: KILL)''\n\t')

    # print attacks
    for i in range(1, 5):
        print('\t' + str(i) + ')' + attacks[i - 1])

    # interpret and calculate damage dealt
    user_input = input('\n\t  ')

    # aggressive (well rounded attack damage/hit chance)
    if user_input == '1':
        min_damage = weapon.base_damage + int(dex / 6)
        max_damage = min_damage + int(strength / 8)
        damage = randint(min_damage, max_damage)
        hit_chance = int(dex + (spd * 2) - (m_spd * (2 / 3)))
        dodge_chance = int(spd / 4) - int(m_spd / 8)
    # defensive (good hit chance, lower damage, can set up for an assisted flee, good dodge chance)
    elif user_input == '2':
        min_damage = weapon.base_damage + int(dex / 7)
        max_damage = min_damage + int(strength / 12)
        damage = randint(min_damage, max_damage)
        hit_chance = int(dex + (spd * 2) - (m_spd * (2 / 3)))  # same hit chance as aggressive
        dodge_chance = int(spd * 2 / 3) - int(m_spd / 12)
    # quick (high hit chance, low damage, high dodge chance)
    elif user_input == '3':
        min_damage = int(.85 * weapon.base_damage) + int(dex / 4)
        max_damage = min_damage + int(strength / 16)
        damage = randint(min_damage, max_damage)
        hit_chance = int(dex + (spd * 3) - (m_spd * (1 / 3)))
        dodge_chance = spd - int(m_spd / 8)
    # power (lower hit chance, high damage, can inflict debuffs)
    elif user_input == '4':
        min_damage = int(weapon.base_damage) + int(dex / 6)
        max_damage = min_damage + int(strength / 2)
        damage = randint(min_damage, max_damage)
        hit_chance = int((dex * 2) + (spd / 2) - (m_spd))
        dodge_chance = int(spd / 16)

        # try to strike bleed status effect
        if randint(0, 4) == 1:
            debuff = codex.STATUS_EFFECTS_DATA['Bleed']
            print('You have inflicted Bleed on the enemy!')

    elif user_input == '5':
        hit_chance = 1000
        damage = 1000

    # roll for successful hit
    if randint(0, 100) <= hit_chance:
        # apply damage to monster
        monster.health -= (damage)
        print('\nYou attack the ' + monster.race + ', doing ' + str(damage) + ' damage!\n')
    else:
        print('\nYou attack the ' + monster.race + ', but it dodges your attack!\n')

    sleep(.6)

    # roll for dodge
    if randint(0, 100) >= dodge_chance:
        # calculate and apply damage to player (RUDIMENTARY)
        min_monster_damage = int((m_strength / 12) + (m_dex / 8))
        max_monster_damage = int((m_strength / 6) + (m_dex / 6))
        monster_damage = randint(min_monster_damage, max_monster_damage)
        player_model.health -= monster_damage
        print('The ' + monster.race + ' attacks you, doing ' + str(monster_damage) + ' damage!\n')
    else:
        print('The ' + monster.race + ' attacks you, But you dodge its attack!\n')

    sleep(.6)

    return debuff


# start a combat encounter
def combat_encounter():
    global battle_modifier

    # give the player a wooden sword if they have no weapon (DEBUG)
    if player_model.equipment['Weapon'] is None:
        player_model.equipment['Weapon'] = itf.create_weapon('Practice Sword')

    # Create a random beast monster
    monster = cf.create_creature_from_race(cf.random_race_from_family('Beast'), 10)
    monster_status_effects = []

    # display encounter message
    print('\nA wild ' + monster.race + ' appears!\n')

    sleep(.5)

    # main combat loop, continues until monster is dead or player flees
    while monster.health > 0:

        battle_modifier = 'New Battle'

        # apply status effects
        if monster_status_effects.__len__() > 0:
            for effect in monster_status_effects:
                drain = effect['hp_drain']
                monster.health -= int(drain)
                print('Monster lost ' + drain + ' hp from bleeding!')

        print('You have ' + str(player_model.health) + ' hp. Your enemy has ' + str(monster.health) + '.')

        # display combat options
        user_input = input('What will you do?\n'
                           '\n\t1) flee'
                           '\n\t2) attack'
                           '\n\t3) ability (UNFINISHED)'
                           '\n\t4) item (UNFINISHED)\n\n\t  ')

        # flee attempt
        if user_input == '1':
            if commands[user_input](monster):
                break
        # attack prompt
        elif user_input == '2':
            debuff = commands[user_input](monster)

            if debuff is not None:
                monster_status_effects.append(debuff)

    # monster is dead, not fled
    if monster.health < 0:
        print('You have defeated the ' + monster.race + '.')
        sleep(.6)

        player_model.weapon_proficiencies[player_model.equipment['Weapon'].weapon_type] += 1

        # get random monster drop
        r = randint(0, 100)
        drop = None
        for code, percent in monster.loot_rates.items():
            if r < int(percent):
                drop = itf.create_ingredient(code)

        # insert drop to player inventory
        if drop is not None:
            print('It dropped a ' + drop.name + '.')
            player_mediator.add_item(drop)
            sleep(.6)


commands = {
    '1': try_flee,
    '2': attack_prompt,
    '3': None,  # TODO abilities (Taunt, etc)
    '4': None  # TODO Consumable and weapon switch
}
