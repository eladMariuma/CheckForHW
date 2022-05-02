# Packages needed for this assignment
import gym
import numpy as np
import time
import matplotlib.pyplot as plt
from IPython.display import clear_output  # Used to clear the output of a Jupyter cell.

def randomAgent(start_state):
    env.s = start_state  # set environment to illustration's state
    epochs = 0
    penalties, reward = 0, 0

    frames = []  # for animation
    visited = []
    rewards = 0
    done = False
    while not done:
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)

        while state in visited:
            action = env.action_space.sample()
            state, reward, done, info = env.step(action)

        visited.append(state)
        rewards += reward
        if reward == -10:
            penalties += 1

        # Put each rendered frame into dict for animation
        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
        }
        )

        epochs += 1
    return (frames, rewards)

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        time.sleep(0.1)


if __name__ == '__main__':
    env = gym.make('Taxi-v3').env
    state = env.reset()
    print('Initial state:', state)
    env.reset()  # reset environment to a new, random state
    env.render()

    print("Action Space {}".format(env.action_space))
    print("State Space {}".format(env.observation_space))
    new_state, reward, done, info = env.step(1)  # Take action 1 (north)
    env.render()
    print("New state:", new_state)
    print("Reward:", reward)
    print("Done:", done)
    print("Info:", info)

    #randomAgent
    frames, reward = randomAgent(328)
    print("Reward incurred: {}".format(reward))
    a = 1

# use the algorithm learnt in class
# should return (frames,reward)

def bfs(first_state):
  # add implementation
  return 0       # remove mewedwd


"""
# driver code - for your use only, do not submit these lines!
env.s = 328
frames,reward = bfs(env.s)
print_frames(frames)
print(reward)
"""