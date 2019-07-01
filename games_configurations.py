import networks
import models
import tr_helpers

roboschoolant_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5*1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 1800,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolAnt-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : True,
    'LR_THRESHOLD' : 0.02,
    'NORMALIZE_INPUT' : False
}

roboschoolhumanoid_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.default_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5*1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolHumanoid-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 512,
    'MINIBATCH_SIZE' : 2048,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}


carracing_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5*1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'CarRacing-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 1024,
    'MINIBATCH_SIZE' : 2048,
    'MINI_EPOCHS' : 8,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}


quadrupped_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo2',
    'SCORE_TO_WIN' : 350000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'QuadruppedWalk-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False,
    'NORMALIZE_INPUT' : False
}


quadrupped_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.simple_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo2',
    'SCORE_TO_WIN' : 350000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'QuadruppedWalk-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False,
    'NORMALIZE_INPUT' : False
}

bipedalwalker_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 300,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalker-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 8,
    'CRITIC_COEF' : 1,
    'IS_ADAPTIVE_LR' : True,
    'LR_THRESHOLD' : 0.01,
    'NORMALIZE_INPUT' : True
}

bipedalwalker_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 320,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalker-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'IS_ADAPTIVE_LR' : False,
    'LR_THRESHOLD' : 0.02,
    'NORMALIZE_INPUT' : True
}

bipedalwalkerhardocre_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 320,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalkerHardcore-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'IS_ADAPTIVE_LR' : False,
    'LR_THRESHOLD' : 0.02,
    'NORMALIZE_INPUT' : True
}

pendulum_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.simple_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5e-5,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 0,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.00,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'Pendulum-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False,
    'LR_THRESHOLD' : 0.75,
    'NORMALIZE_INPUT' : False
}


bipedalwalkerhardcore_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 300,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalkerHardcore-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'IS_ADAPTIVE_LR' : True,
    'LR_THRESHOLD' : 0.008,
    'NORMALIZE_INPUT' : True
}

loonar_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.default_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'LunarLanderContinuous-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : False,
    'IS_ADAPTIVE_LR' : False
}

mountain_car_cont_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.001,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCarContinuous-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}

pendulum_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 0,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.00,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'Pendulum-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False,
    'LR_THRESHOLD' : 0.75,
    'NORMALIZE_INPUT' : False
}

mountain_car_config = {
    'NETWORK' : models.ModelA2C(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCar-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 16,
    'MINIBATCH_SIZE' : 64,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}

cartpole_config = {
    'NETWORK' : models.ModelA2C(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'CartPole-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 16,
    'MINIBATCH_SIZE' : 64,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}

car_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.atari_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-3,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'EPISODES_TO_LOG' : 20, 
    'LIVES_REWARD' : 5,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCarContinuous-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}

atari_pong_config = {
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'NETWORK' : models.ModelA2C(networks.atari_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'pong',
    'SCORE_TO_WIN' : 20,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'PongNoFrameskip-v4',
    'PPO' : True,
    'E_CLIP' : 0.1,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 3,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'IS_ADAPTIVE_LR' : False
}