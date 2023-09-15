from rl_x.environments.environment_manager import extract_environment_name_from_file, register_environment
from rl_x.environments.gym.classic.cart_pole_v1.create_env import create_env
from rl_x.environments.gym.classic.cart_pole_v1.default_config import get_config


GYM_CLASSIC_CART_POLE_V1 = extract_environment_name_from_file(__file__)
register_environment(GYM_CLASSIC_CART_POLE_V1, get_config, create_env)