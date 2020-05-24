# rl-gym-memo
try OpenAI Gym  

## make environment memo
make virtual environment for this project with [virtualenv](https://www.sejuku.net/blog/68398)
```
mkdir gym_dir
cd gym_dir
virtualenv -p python3.6 gym-env
source gym-env/bin/activate
```
Installing Pybullet-Gym by [this](http://gym.openai.com/docs/)

install openai gym
```
git clone https://github.com/openai/gym.git
cd gym
pip install -e .
cd ..
```
clone this repository
```
git clone https://github.com/Kanazawanaoaki/rl-gym-memo.git
```

check environment
```
cd rl-gym-memo
python test.py
```

## activate virtualenv
before start
```
cd gym_dir
source gym-env/bin/activate
```

## try mujoco env
Some environments in Gym  use mujoco. If you want to use those envs, you need to install mujoco along [this gide](https://github.com/openai/mujoco-py#install-mujoco).  
In my case, I need to some extra install as bellow.
```
sudo apt-get install libosmesa6-dev
sudo apt install patchelf
```

## try baselines
OpenAI offeres implementations of some algorithms. we can use these implementations from [github](https://github.com/openai/baselines)
```
# in gym_dir
git clone https://github.com/openai/baselines.git
pip install tensorflow==1.14 # if you don't install tensorflow yet
pip install -e .
```
