#!/bin/bash
python example.py \
    --config.runner.track_tb=True \
    --config.runner.track_wandb=True \
    --config.runner.save_model=True \
    --config.runner.wandb_entity="placeholder" \
    --config.runner.project_name="placeholder" \
    --config.runner.exp_name="placeholder" \
    --config.algorithm.total_timesteps=10000 \
    --config.algorithm.nr_envs=2 \
    --config.environment.seed=0

python example.py \
    --config.runner.track_tb=True \
    --config.runner.track_wandb=True \
    --config.runner.save_model=True \
    --config.runner.wandb_entity="placeholder" \
    --config.runner.project_name="placeholder" \
    --config.runner.exp_name="placeholder" \
    --config.algorithm.total_timesteps=10000 \
    --config.algorithm.nr_envs=2 \
    --config.environment.seed=1

echo "finished"