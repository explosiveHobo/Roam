import player_mediator as pm
import combat_mediator as cm


# print reminders of action commands
def print_actions():
    print('Actions listed below'
          '\n\t\"help\": Display actions'
          '\n\t\"quit\": End game'
          '\n\t\"inv\": Show inventory'
          '\n\t\"survey\": Display movement options'
          '\n\t\"move (west/east/north/south)\": Move towards a new location')


# continuously prompt user for commands and run commands
def prompt_action():
    print('Your consciousness awakens at ' + pm.get_location().name)
    pm.survey()

    # primary game loop
    while True:
        user_input = input('What is your action?\n\n\t')

        if user_input == 'quit':
            break
        elif user_input.__contains__('move'):
            if not pm.move(user_input):
                cm.combat_encounter()

            print('\nYou have arrived at ' + pm.get_location().name)

        elif commands.__contains__(user_input):
            commands[user_input]()


commands = {
    'help': print_actions,
    'survey': pm.survey,
    'inv': pm.print_inventory
}
