from stable_baselines.common.cmd_util import make_atari_env
from stable_baselines.common.vec_env import VecFrameStack
from stable_baselines import ACER

import matplotlib.pyplot as plt

# There already exists an environment generator
# that will make and wrap atari environments correctly.
# Here we are also multiprocessing training (num_env=4 => 4 processes)
env = make_atari_env('PongNoFrameskip-v4', num_env=4, seed=0)
# Frame-stacking with 4 frames
env = VecFrameStack(env, n_stack=4)

# model = ACER('CnnPolicy', env, verbose=1)
# model.learn(total_timesteps=25000)

# # save 
# model.save("cnn_pong")

# load
model = ACER.load("cnn_pong")
print(model)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    print(rewards)
    # env.render()
    # env.render(mode='rgb_array')
    img =env.render(mode='rgb_array')
    plt.imshow(img)
    print(type(img))
    plt.show()
