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
