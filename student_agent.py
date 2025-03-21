from auxiliary_definitions import *

import numpy as np
import pickle
import gym

q_table = None
with open("b10902091_q_table.pkl", "rb") as file:
    q_table = pickle.load(file)
assert q_table is not None, "Failed to load Q-table."

def get_action(obs):
    assert q_table is not None, "Failed to load Q-table."

    observations = Observations(obs)
    state = State(
        observations.obstacle_north,
        observations.obstacle_south,
        observations.obstacle_east,
        observations.obstacle_west,
    )
    action = np.argmax(q_table[state])

    return action