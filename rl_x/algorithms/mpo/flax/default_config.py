from ml_collections import config_dict


def get_config(algorithm_name):
    config = config_dict.ConfigDict()

    config.algorithm_name = algorithm_name

    config.device = "gpu"  # cpu, gpu
    config.total_timesteps = 1e9
    config.agent_learning_rate = 3e-4
    config.dual_learning_rate = 1e-2
    config.anneal_agent_learning_rate = False
    config.anneal_dual_learning_rate = False
    config.buffer_size = 1e6
    config.learning_starts = 5000
    config.batch_size = 256
    config.tau = 0.005
    config.gamma = 0.99
    config.init_log_temperature = 10.0
    config.init_log_alpha_mean = 10.0
    config.init_log_alpha_stddev = 1000.0
    config.trace_length = 8
    config.ensemble_size = 2
    config.log_std_min = -20
    config.log_std_max = 2
    config.nr_hidden_units = 256
    config.logging_freq = 3000

    return config
