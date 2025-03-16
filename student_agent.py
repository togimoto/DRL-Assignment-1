# Remember to adjust your student ID in meta.xml
import numpy as np
import pickle
import random
import gym

from enum import IntEnum
from dataclasses import dataclass

class Actions(IntEnum):
    MOVE_SOUTH = 0
    MOVE_NORTH = 1
    MOVE_EAST = 2
    MOVE_WEST = 3
    PICK_UP = 4
    DROP_OFF = 5

@dataclass
class Observations:
    taxi_pos: tuple
    R: tuple
    G: tuple
    Y: tuple
    B: tuple
    obstacle_north: int
    obstacle_south: int
    obstacle_east: int
    obstacle_west: int
    near_passenger: int
    near_dest: int

    def __init__(self, obs):
        self.taxi_pos = (obs[0], obs[1])
        self.R = (obs[2], obs[3])
        self.G = (obs[4], obs[5])
        self.Y = (obs[6], obs[7])
        self.B = (obs[8], obs[9])
        self.obstacle_north = obs[10]
        self.obstacle_south = obs[11]
        self.obstacle_east = obs[12]
        self.obstacle_west = obs[13]
        self.near_passenger = obs[14]
        self.near_dest = obs[15]

def get_action(obs):
    
    # TODO: Train your own agent
    # HINT: If you're using a Q-table, consider designing a custom key based on `obs` to store useful information.
    # NOTE: Keep in mind that your Q-table may not cover all possible states in the testing environment.
    #       To prevent crashes, implement a fallback strategy for missing keys. 
    #       Otherwise, even if your agent performs well in training, it may fail during testing.


    return random.choice([0, 1, 2, 3, 4, 5]) # Choose a random action
    # You can submit this random agent to evaluate the performance of a purely random strategy.

