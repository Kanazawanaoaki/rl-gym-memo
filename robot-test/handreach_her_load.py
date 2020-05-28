import numpy as np
import gym

from stable_baselines import HER, SAC, DDPG, TD3
from stable_baselines.her import GoalSelectionStrategy, HERGoalEnvWrapper
from stable_baselines.ddpg import NormalActionNoise

env = gym.make('HandReach-v0')
obs = env.reset()
done = False

model_class = DDPG

# Available strategies (cf paper): future, final, episode, random
goal_selection_strategy = 'future' # equivalent to GoalSelectionStrategy.FUTURE

# Wrap the model
model = HER('MlpPolicy', env, model_class, n_sampled_goal=4, goal_selection_strategy=goal_selection_strategy,verbose=1)

# Train the model
# model.learn(500000)

# model.save("hand_reach_her_env")

model = HER.load('hand_reach_her_env', env=env)

obs = env.reset()
for _ in range(500):
    env.render()
    action, _ = model.predict(obs)
    obs, reward, done, _ = env.step(action)

    if done:
        obs = env.reset()



# while not done:
#     env.render()
#     action = policy(obs['observation'], obs['desired_goal'])
#     obs, reward, done, info = env.step(action)

#     # If we want, we can substitute a goal here and re-compute
#     # the reward. For instance, we can just pretend that the desired
#     # goal was what we achieved all along.
#     substitute_goal = obs['achieved_goal'].copy()
#     substitute_reward = env.compute_reward(
#         obs['achieved_goal'], substitute_goal, info)
#     print('reward is {}, substitute_reward is {}'.format(
#         reward, substitute_reward))
