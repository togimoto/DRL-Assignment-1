from auxiliary_definitions import *

import numpy as np
from collections import defaultdict
from pprint import pp
import pickle
import os

def generate_initial_state() -> tuple[int, int, int, int]:
    while True:
        random_0_1 = np.random.choice((0,1), 4)
        assert np.sum(random_0_1) <= 4
        if np.sum(random_0_1) < 4:
            # has at least one valid move
            break
    # convert to tuple to avoid pickling error
    return tuple( State( *tuple( random_0_1.tolist() ) ) )

def train(
    *,
    input_filename=None,
    output_filename=None,
    episodes=10000,
    epsilon_start=1.0,
    epsilon_end=0, # decay to 0 to verify performance
    decay_rate=0.9992,
) -> None:
    empty_q_table_row = lambda: [0.] * len(Actions)
    if input_filename:
        with open(input_filename, "rb") as file:
            q_table = defaultdict(empty_q_table_row, pickle.load(file))
            print(f"Q-table loaded from {input_filename}")
    else:
        q_table = defaultdict(empty_q_table_row)

    rewards_per_episode = []
    epsilon = epsilon_start

    for episode in range(episodes):
        state = generate_initial_state()

        if np.random.uniform(0, 1) <= epsilon:
            action = int(np.random.choice(list(Actions)))
        else:
            action = np.argmax(q_table[state])

        did_not_move = action in (Actions.PICK_UP, Actions.DROP_OFF)
        hit_obstacle = did_not_move or state[ action_to_state_mapping[action] ] == 1
        if did_not_move or hit_obstacle:
            reward = -1
        else:
            reward = 1
        rewards_per_episode.append(reward)

        q_table[state][action] += reward - q_table[state][action]
        epsilon = max(epsilon_end, epsilon * decay_rate)

        if (episode + 1) % 100 == 0:
            avg_reward = np.mean(rewards_per_episode[-100:])
            print(f"Episode {episode + 1}/{episodes}, Avg Reward: {avg_reward:.4f}, Epsilon: {epsilon:.3f}", flush=True)

    # must convert defaultdict back to dict to avoid pickling errors when
    # q-table is loaded in another module
    q_table = dict(q_table)

    print("Training complete. Final Q-table:")
    pp(q_table)

    if output_filename:
        save_file = True
        if os.path.exists(output_filename):
            response = input(f"{output_filename} already exists. Overwrite? (y/n): ")
            save_file = True if response == "y" else False
        if save_file:
            with open(output_filename, 'wb') as file:
                pickle.dump(q_table, file, protocol=pickle.HIGHEST_PROTOCOL)
                print(f"Q-table saved to {output_filename}.")

if __name__ == "__main__":
    train(output_filename="b10902091_q_table.pkl")