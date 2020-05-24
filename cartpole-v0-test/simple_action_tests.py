import gym
env = gym.make('CartPole-v0')
finished_timesteps =[]
for i_episode in range(20):
    observation = env.reset()
    for t in range(300):
        env.render()
        # print(observation)
        ############## test action No.1
        # action = env.action_space.sample()
        ############## test action No.2
        # action = 0
        # if observation[2]>0:
        #     action = 1
        ############## test action No.3
        action = 0
        if observation[1]<-0.7:
            action = 1
        elif observation[1]>0.7:
            action = 0
        elif observation[2]>0:
            action = 1
        ################
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            finished_timesteps.append(t+1)
            break
env.close()
print("Average of finished timesteps : {}".format(sum(finished_timesteps)/len(finished_timesteps)))
