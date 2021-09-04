import player_model
import world
import codex
import action_mediator

# read in static data (csv & txt)
codex.initialize()

root = world.generate_world(15)

player_model.location = root

action_mediator.prompt_action()
