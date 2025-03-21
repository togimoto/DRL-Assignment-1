from enum import IntEnum
from collections import namedtuple, defaultdict
from dataclasses import dataclass

class Actions(IntEnum):
    MOVE_SOUTH = 0
    MOVE_NORTH = 1
    MOVE_EAST = 2
    MOVE_WEST = 3
    PICK_UP = 4
    DROP_OFF = 5

State = namedtuple("State", "obstacle_north obstacle_south obstacle_east obstacle_west")

action_to_state_mapping = {
    Actions.MOVE_NORTH: State._fields.index("obstacle_north"),
    Actions.MOVE_SOUTH: State._fields.index("obstacle_south"),
    Actions.MOVE_EAST: State._fields.index("obstacle_east"),
    Actions.MOVE_WEST: State._fields.index("obstacle_west"),
}

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