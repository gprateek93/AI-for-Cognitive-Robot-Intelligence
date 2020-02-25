import random 

class Agent:
    def __init__(self,initial_state):
        self.state = initial_state
    
    def transition(self, state, n):
        r = random.random()
        new_state = ()

        #All the actions are equally likely
        if(r <= 0.25): #moves up the grid
            new_state  = (state[0]-1,state[1]) if state[0]>0 else state
        elif(r <= 0.5): #moves down the grid
            new_state  = (state[0]+1,state[1]) if state[0]<(n-1) else state
        elif(r <= 0.75): #moves left of the grid
            new_state  = (state[0],state[1]-1) if state[1]>0 else state
        else: #move right of the grid
            new_state  = (state[0],state[1]+1) if state[1]<n-1 else state
        self.state = new_state
        return new_state
    
