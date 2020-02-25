import random
import math
import numpy as np 

rotor_sound_strong = [(1, 0), (1, 2), (1, 3), (2, 0), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (4, 3)]
rotor_sound_weak = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 4), (2, 1), (3, 0), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 4)]
bump_sound_strong = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3)]
bump_sound_weak = [(0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 4)]

def get_emission_prob(observation, state,mode):
    res = 0
    if mode == 1: #mode=1 means that both bump and rotor observations are taken into consideration
        if state in rotor_sound_strong and state in bump_sound_strong:
            if observation == (0,0):
                res = 0.1 * 0.1
            elif observation == (0,1):
                res = 0.1 * 0.9
            elif observation == (1,0):
                res = 0.9 * 0.1
            else:
                res = 0.9 * 0.9
        elif state in rotor_sound_strong and state in bump_sound_weak:
            if observation == (0,0):
                res = 0.1 * 0.9
            elif observation == (0,1):
                res = 0.1 * 0.1
            elif observation == (1,0):
                res = 0.9 * 0.9
            else:
                res = 0.9 * 0.1
        elif state in rotor_sound_weak and state in bump_sound_strong:
            if observation == (0,0):
                res = 0.9 * 0.1
            elif observation == (0,1):
                res = 0.9 * 0.9
            elif observation == (1,0):
                res = 0.1 * 0.1
            else:
                res = 0.1 * 0.9
        else:
            if observation == (0,0):
                res = 0.9 * 0.9
            elif observation == (0,1):
                res = 0.9 * 0.1
            elif observation == (1,0):
                res = 0.1 * 0.9
            else:
                res = 0.1 * 0.1
    else:#If only bump observations were taken into consideration
        if state in bump_sound_strong:
            if observation[1] == 0:
                res = 0.1
            else:
                res = 0.9
        else:
            if observation[1] == 0:
                res = 0.9
            else:
                res = 0.1
    # print(res)
    return res

def valid(state, grid_size):
    if state[0]>=0 and state[0] < grid_size and state[1] >=0 and state[1] < grid_size:
        return True
    else:
        return False

def filtering(init_grid,num_of_time_steps, grid_size, observations):
    forward_pass = [init_grid]
    transition_x = [1,0,-1,0]
    transition_y = [0,1,0,-1]
    for i in range(num_of_time_steps):
        ith_grid = []
        for j in range(grid_size):
            jth_row = []
            for k in range(grid_size):
                sum = 0.0
                for l in range(4):
                    x = j + transition_x[l]
                    y = k + transition_y[l]
                    if valid((x,y),grid_size):
                        sum += 0.25 * forward_pass[i][x][y]
                    else:
                        sum += 0.25 * forward_pass[i][j][k]
                value = get_emission_prob(observations[i+1],(j,k),2) * sum
                jth_row.append(value)
            ith_grid.append(jth_row)
        forward_pass.append(ith_grid)
    return forward_pass

def get_log_likelihood(forward_pass, grid_size):
    ll = []
    for i in range(len(forward_pass)):
        ith_grid = []
        for j in range(grid_size):
            jth_row = []
            for k in range(grid_size):
                jth_row.append(math.log(forward_pass[i][j][k]))
            ith_grid.append(jth_row)
        ll.append(ith_grid)
    return ll

def maximum_likelihood(forward_pass,grid_size,init_state):
    mle = [init_state]
    for i in range(len(forward_pass)):
        ma = -math.inf
        state = (-1,-1)
        for j in range(grid_size):
            for k in range(grid_size):
                if ma < forward_pass[i][j][k]:
                    state = (j,k)
                    ma = forward_pass[i][j][k]
        if i!=0:
           mle.append(state)
    return mle 

def prediction(num_of_time_steps, grid_size, curr_state_dist):
    transition_x = [1,0,-1,0]
    transition_y = [0,1,0,-1]
    predictive_states = [curr_state_dist]
    for i in range(num_of_time_steps):
        ith_grid = []
        for j in range(grid_size):
            jth_row = []
            for k in range(grid_size):
                sum = 0.0
                for l in range(4):
                    x = j + transition_x[l]
                    y = k + transition_y[l]
                    if valid((x,y),grid_size):
                        sum += 0.25 * predictive_states[i][x][y]
                    else:
                        sum += 0.25 * predictive_states[i][j][k]
                value = sum
                jth_row.append(value)
            ith_grid.append(jth_row)
        predictive_states.append(ith_grid)
    return predictive_states
            
        

def backward(num_of_time_steps, grid_size, observations):
    init_grid = [[1 for i in range(grid_size)]for j in range(grid_size)]
    transition_x = [1,0,-1,0]
    transition_y = [0,1,0,-1]
    backward_pass = [init_grid]
    for i in range(num_of_time_steps):
        ith_grid = []
        for j in range(grid_size):
            jth_row = []
            for k in range(grid_size):
                sum = 0.0
                for l in range(4):
                    x = j + transition_x[l]
                    y = k + transition_y[l]
                    if valid((x,y),grid_size):
                        emission = get_emission_prob(observations[-i-1],(x,y),1)
                        sum += emission * 0.25 * backward_pass[i][x][y]
                    else:
                        emission = get_emission_prob(observations[-i-1],(j,k),1)
                        sum += emission * 0.25 * backward_pass[i][j][k]
                value = sum
                jth_row.append(value)
            ith_grid.append(jth_row)
        backward_pass.append(ith_grid)
    return backward_pass

def smoothing(num_of_time_steps,grid_size,forward_pass, backward_pass):
    smoothing_variable = []
    for i in range(num_of_time_steps):
        forward_pass_i = np.array(forward_pass[i])
        backward_pass_i = np.array(backward_pass[-i-1])
        sv = np.multiply(forward_pass_i,backward_pass_i)
        sv = (sv - np.min(sv))/(np.max(sv)-np.min(sv))
        smoothing_variable.append(sv.tolist())

    return smoothing_variable