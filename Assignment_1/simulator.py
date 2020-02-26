from environment import *
from agent import *
import utils
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbn

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

def generate_heat_map(strong,weak,grid_size):
    h_map = []
    for i in range(grid_size):
        ith_row = []
        for j in range(grid_size):
            if((i,j) in strong):
                ith_row.append(0.9)
            else:
                ith_row.append(0.1)
        h_map.append(ith_row)
    ax = plt.axes()
    sbn.heatmap(h_map,cmap = "PiYG",ax = ax)
    plt.show()


def main(init_state,grid_size,time_steps,time_steps_prediction):

    generate_heat_map(utils.rotor_sound_strong,utils.rotor_sound_weak,grid_size)
    generate_heat_map(utils.bump_sound_strong,utils.bump_sound_weak,grid_size)

    agent,env = init(init_state,grid_size)
    states,observations = simulate(agent,env,time_steps)
    # states = [(2, 2), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 2), (3, 2), (3, 3), (3, 2), (2, 2)]
    # observations = [(0, 0), (1, 1), (0, 1), (0, 0), (1, 0), (1, 0), (1, 0), (0, 0), (1, 1), (0, 0), (0, 1)]
    # states = [(2, 2), (3, 2), (2, 2), (2, 3), (1, 3), (1, 4), (1, 4), (2, 4), (2, 3), (3, 3), (3, 2)]
    # observations = [(1, 1), (1, 0), (1, 1), (1, 1), (1, 0), (0, 0), (0, 0), (1, 0), (1, 1), (0, 0), (1, 0)]

    print(states)
    print(observations)
    print("going in utils")
    init_pass = [[1/math.pow(grid_size,2) for i in range(grid_size)] for j in range(grid_size)]
    forward_pass = utils.filtering(init_pass,time_steps,grid_size,observations)
    # ll = utils.get_log_likelihood(forward_pass,grid_size)
    # predictions = utils.prediction(time_steps_prediction,grid_size,forward_pass[-1])
    # print(predictions)
    # backward_pass = utils.backward(time_steps,grid_size,observations)
    # print(backward_pass)
    # print(len(backward_pass))
    # smoothing_var = utils.smoothing(time_steps,grid_size, forward_pass,backward_pass)
    # print(smoothing_var)
    # viterbi_pass = utils.viterbi(init_pass,time_steps,grid_size,observations)
    # print(viterbi_pass)
    for i in range(len(forward_pass)):
        ax = plt.axes()
        sbn.heatmap(forward_pass[i],annot = True,cmap = "PiYG",ax = ax)
        ax.set_title("Timestep " + str(i))
        plt.savefig("Timestep " + str(i))
        plt.clf()
        # plt.show()
    mle = utils.maximum_likelihood(forward_pass,grid_size,init_state)
    distinguish = [[[0 for i in range(grid_size)] for j in range(grid_size)] for k in range(time_steps+1)]
    for i in range(time_steps+1):
        distinguish[i][states[i][0]][states[i][1]] = 1
        distinguish[i][mle[i][0]][mle[i][1]] = -1
        ax = plt.axes()
        sbn.heatmap(distinguish[i],annot = True,cmap = "PiYG",ax = ax)
        ax.set_title("Difference at timestep " + str(i))
        plt.savefig("d_Timestep " + str(i))
        plt.show()
    
    error = utils.compute_manhattan_error(states,mle)
    #plot error:
    x = range(len(states))
    plt.plot(x,error)
    plt.xlabel("Time Steps")
    plt.ylabel("Manhattan error in estimation of robot's location")
    plt.title("Error in tracking of robots over different time-steps")
    plt.show()

    print(mle)

main((2,2),25,10,5)