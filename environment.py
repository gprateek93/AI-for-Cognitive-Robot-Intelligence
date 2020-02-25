import random
from utils import rotor_sound_strong,bump_sound_strong


class Environment:
    def __init__(self,grid_size):
        self.grid_size = grid_size
    
    def get_message(self,state):
        rotor_message = ""
        bump_message = ""
        #compute message signals
        r = random.random()
        if state in rotor_sound_strong:
            if r<=0.9:
                rotor_message = 1
            else:
                rotor_message = 0
        else:
            if r<=0.1:
                rotor_message = 1
            else:
                rotor_message = 0

        if state in bump_sound_strong:
            if r<=0.9:
                bump_message = 1
            else:
                bump_message = 0
        else:
            if r<=0.1:
                bump_message = 1
            else:
                bump_message = 0
        return (rotor_message,bump_message)

