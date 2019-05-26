from src.World import *
import random


def get_action(world: World):
    actions = ['u', 'd', 'l', 'r']
    action = actions[random.randint(0, 3)]
    return action
