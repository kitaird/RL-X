from rl_x.environments.environment_manager import extract_environment_name_from_file, register_environment
from rl_x.environments.gym.mujoco.humanoid_v4.create_env import create_env
from rl_x.environments.gym.mujoco.humanoid_v4.default_config import get_config


GYM_MUJOCO_HUMANOID_V4 = extract_environment_name_from_file(__file__)
register_environment(GYM_MUJOCO_HUMANOID_V4, get_config, create_env)
