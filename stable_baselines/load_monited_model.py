import gym

from stable_baselines import DDPG

env = gym.make('LunarLanderContinuous-v2')

# Load the trained agent
model = DDPG.load("tmp/best_model")

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
