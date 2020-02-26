import random
import math
import numpy as np 

# rotor_sound_strong = [(1, 0), (1, 2), (1, 3), (2, 0), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (4, 3)]
rotor_sound_strong = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 24), (2, 25), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 19), (3, 20), (3, 21), (3, 22), (3, 23), (3, 24), (3, 25), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (4, 19), (4, 20), (4, 21), (4, 22), (4, 23), (4, 24), (4, 25), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (5, 18), (5, 19), (5, 20), (5, 21), (5, 22), (5, 23), (5, 24), (5, 25), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16), (6, 17), (6, 18), (6, 19), (6, 20), (6, 21), (6, 22), (6, 23), (6, 24), (6, 25), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18), (7, 19), (7, 20), (7, 21), (7, 22), (7, 23), (7, 24), (7, 25), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22), (13, 22), (13, 23), (13, 24), (13, 25), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (14, 24), (14, 25), (15, 16), (15, 17), (15, 18), (15, 19), (15, 20), (15, 21), (15, 22), (15, 23), (15, 24), (15, 25), (16, 17), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (16, 24), (16, 25), (17, 18), (17, 19), (17, 20), (17, 21), (17, 22), (17, 23), (17, 24), (17, 25), (18, 19), (18, 20), (18, 21), (18, 22), (18, 23), (18, 24), (18, 25), (19, 20), (19, 21), (19, 22), (19, 23)]
bump_sound_strong = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19), (2, 20), (2, 21), (2, 22), (2, 23), (2, 24), (2, 25), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 19), (3, 20), (3, 21), (3, 22), (6, 16), (6, 17), (6, 18), (6, 19), (6, 20), (6, 21), (6, 22), (6, 23), (6, 24), (6, 25), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18), (7, 19), (7, 20), (7, 21), (7, 22), (7, 23), (7, 24), (7, 25), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22), (8, 23), (8, 24), (8, 25), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18), (9, 19), (9, 20), (9, 21), (9, 22), (9, 23), (9, 24), (9, 25), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (10, 19), (10, 20), (10, 21), (10, 22), (10, 23), (10, 24), (10, 25), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16), (11, 17), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22), (11, 23), (11, 24), (11, 25), (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (12, 18), (12, 19), (12, 20), (12, 21), (12, 22), (12, 23), (12, 24), (12, 25), (13, 14), (13, 15), (13, 16), (13, 17), (13, 18), (13, 19), (13, 20), (13, 21), (13, 22), (13, 23), (13, 24), (13, 25), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (14, 24), (14, 25), (15, 16), (15, 17), (15, 18), (15, 19), (15, 20)]
# rotor_sound_weak = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (1, 4), (2, 1), (3, 0), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 4)]
# bump_sound_strong = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 2), (2, 3), (4, 1), (4, 2), (4, 3)]
# bump_sound_weak = [(0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 4)]
rotor_sound_weak = [(20, 25), (10, 17), (13, 17), (8, 24), (9, 21), (11, 22), (10, 18), (12, 17), (13, 20), (23, 25), (9, 14), (10, 13), (19, 24), (10, 24), (9, 16), (11, 21), (10, 23), (12, 22), (22, 25), (10, 14), (11, 15), (9, 19), (21, 24), (11, 16), (22, 23), (9, 25), (12, 13), (20, 21), (13, 16), (12, 24), (8, 25), (9, 20), (10, 19), (12, 18), (13, 19), (23, 24), (9, 13), (10, 25), (9, 23), (24, 25), (11, 20), (10, 20), (12, 23), (11, 25), (10, 15), (11, 14), (9, 18), (11, 19), (12, 20), (9, 11), (9, 24), (11, 13), (12, 14), (20, 22), (13, 15), (12, 25), (21, 23), (20, 24), (10, 16), (12, 19), (13, 18), (9, 12), (10, 11), (8, 23), (9, 22), (11, 23), (10, 21), (12, 16), (11, 24), (13, 21), (9, 15), (10, 12), (19, 25), (9, 17), (11, 18), (10, 22), (12, 21), (22, 24), (9, 10), (11, 12), (21, 25), (12, 15), (11, 17), (20, 23), (13, 14), (21, 22)]
bump_sound_weak = [(6, 9), (20, 25), (7, 12), (17, 20), (7, 25), (18, 19), (17, 25), (8, 24), (9, 21), (14, 18), (11, 22), (10, 18), (12, 17), (13, 20), (4, 10), (2, 6), (5, 11), (4, 5), (3, 23), (5, 24), (4, 16), (19, 24), (6, 23), (5, 21), (7, 22), (16, 19), (17, 18), (22, 25), (18, 25), (8, 12), (10, 14), (8, 18), (14, 21), (11, 15), (9, 19), (15, 16), (11, 16), (1, 21), (2, 18), (3, 11), (1, 15), (4, 12), (2, 12), (3, 17), (6, 14), (7, 15), (20, 21), (7, 24), (17, 24), (8, 25), (9, 20), (15, 25), (14, 19), (10, 19), (12, 18), (1, 19), (13, 19), (2, 24), (4, 11), (3, 5), (2, 7), (5, 10), (4, 6), (3, 22), (5, 7), (4, 17), (6, 20), (5, 20), (7, 17), (16, 20), (18, 22), (8, 13), (10, 15), (8, 19), (11, 14), (9, 18), (15, 19), (11, 19), (1, 20), (12, 20), (2, 19), (1, 25), (13, 25), (3, 10), (1, 14), (4, 13), (2, 13), (4, 24), (3, 16), (6, 15), (19, 21), (7, 14), (6, 18), (20, 22), (21, 23), (15, 24), (14, 16), (10, 16), (15, 21), (12, 19), (1, 18), (13, 18), (2, 25), (1, 7), (5, 9), (4, 7), (3, 25), (5, 6), (4, 18), (6, 21), (5, 19), (7, 16), (6, 24), (16, 21), (16, 24), (18, 23), (8, 14), (9, 15), (10, 12), (8, 20), (9, 17), (15, 18), (11, 18), (10, 22), (12, 21), (2, 16), (1, 24), (13, 24), (3, 13), (1, 13), (4, 14), (2, 10), (5, 15), (4, 25), (3, 19), (6, 12), (4, 20), (19, 20), (7, 9), (6, 19), (21, 25), (20, 23), (21, 22), (14, 17), (10, 17), (15, 20), (1, 17), (13, 17), (2, 22), (1, 6), (3, 7), (2, 5), (1, 11), (5, 8), (3, 24), (6, 7), (4, 19), (6, 10), (5, 18), (7, 19), (6, 25), (16, 22), (17, 23), (16, 25), (18, 20), (8, 15), (23, 25), (9, 14), (10, 13), (8, 21), (14, 24), (10, 24), (9, 16), (14, 15), (11, 21), (10, 23), (12, 22), (2, 17), (13, 23), (3, 12), (1, 12), (4, 15), (2, 11), (5, 14), (3, 18), (6, 13), (4, 21), (19, 23), (7, 8), (6, 16), (21, 24), (7, 21), (22, 23), (8, 9), (9, 25), (14, 22), (15, 23), (12, 13), (1, 16), (13, 16), (12, 24), (2, 23), (1, 5), (3, 6), (1, 10), (6, 11), (5, 17), (7, 18), (16, 23), (17, 22), (18, 21), (23, 24), (9, 13), (8, 22), (14, 25), (10, 25), (9, 23), (24, 25), (11, 20), (10, 20), (12, 23), (11, 25), (13, 22), (3, 15), (4, 8), (2, 8), (5, 13), (3, 21), (4, 22), (19, 22), (7, 11), (6, 17), (5, 23), (7, 20), (16, 17), (8, 10), (9, 11), (9, 24), (8, 16), (14, 23), (11, 13), (15, 22), (12, 14), (1, 23), (13, 15), (12, 25), (2, 20), (3, 9), (2, 3), (1, 9), (2, 14), (6, 8), (5, 16), (20, 24), (7, 13), (17, 21), (9, 12), (10, 11), (8, 23), (9, 22), (11, 23), (10, 21), (12, 16), (11, 24), (13, 21), (3, 14), (4, 9), (2, 9), (5, 12), (3, 20), (5, 25), (4, 23), (19, 25), (7, 10), (6, 22), (5, 22), (7, 23), (16, 18), (17, 19), (22, 24), (18, 24), (8, 11), (9, 10), (8, 17), (14, 20), (11, 12), (15, 17), (12, 15), (11, 17), (1, 22), (13, 14), (2, 21), (3, 8), (1, 8), (2, 15)]

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
                value = get_emission_prob(observations[i+1],(j,k),1) * sum
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

def neighbour(state_1, state_2):
    error = abs(state_1[0]-state_2[0]) + abs(state_1[1]-state_2[1])
    return error<=1

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
                elif i!=0 and ma == forward_pass[i][j][k]:
                    if neighbour((j,k) , mle[i-1]):
                        state = (j,k)
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
    for i in range(num_of_time_steps+1):
        forward_pass_i = np.array(forward_pass[i])
        backward_pass_i = np.array(backward_pass[-i-1])
        sv = np.multiply(forward_pass_i,backward_pass_i)
        sv = (sv - np.min(sv))/(np.max(sv)-np.min(sv))
        smoothing_variable.append(sv.tolist())

    return smoothing_variable

def calculate_initial_prob(init_grid,grid_size,observation):
    for i in range(grid_size):
        for j in range(grid_size):
            init_grid[i][j] *= get_emission_prob(observation,(i,j),1)
    return init_grid

def viterbi(init_grid, num_of_time_steps,grid_size, observations):
    init_grid = calculate_initial_prob(init_grid,grid_size,observations[0])
    viterbi_pass = [init_grid]
    transition_x = [1,0,-1,0]
    transition_y = [0,1,0,-1]
    for i in range(num_of_time_steps):
        ith_grid = []
        for j in range(grid_size):
            jth_row = []
            for k in range(grid_size):
                ma = -math.inf
                for l in range(4):
                    x = j + transition_x[l]
                    y = k + transition_y[l]
                    if valid((x,y),grid_size):
                        ma = max(ma,0.25 * viterbi_pass[i][x][y])
                    else:
                        ma = max(ma,0.25 * viterbi_pass[i][j][k])
                value = ma * get_emission_prob(observations[i+1],(j,k),1)
                jth_row.append(value)
            ith_grid.append(jth_row)
        viterbi_pass.append(ith_grid)
    return viterbi_pass

def compute_manhattan_error(ground_truth, estimations):
    error = []
    for i in range(len(ground_truth)):
        ith_error = abs(ground_truth[i][0] - estimations[i][0]) + abs(ground_truth[i][1] - estimations[i][1])
        error.append(ith_error)
    return error
    