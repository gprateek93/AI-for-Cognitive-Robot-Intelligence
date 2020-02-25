from environment import *
from agent import *
import utils
import math

def init(init_state,grid_size):    
    agent = Agent(init_state)
    environment = Environment(grid_size)
    return agent, environment

def simulate(agent, environment, time_steps):
    observations = [environment.get_message(agent.state)]
    states = [agent.state]
    for i in range(time_steps):
        new_state = agent.transition(agent.state,5)
        states.append(new_state)
        msg = environment.get_message(agent.state)
        observations.append(msg)
    return states, observations

def main(init_state,grid_size,time_steps):
    agent,env = init(init_state,grid_size)
    states,observations = simulate(agent,env,time_steps)
    print(states)
    print(observations)
    print("going in utils")
    init_pass = [[1/math.pow(grid_size,2) for i in range(grid_size)] for j in range(grid_size)]
    forward_pass = utils.filtering(init_pass,time_steps,grid_size,observations)
    ll = utils.get_log_likelihood(forward_pass,grid_size)
    mle = utils.maximum_likelihood(ll,grid_size,init_state)
    print(mle)

main((2,2),5,10)