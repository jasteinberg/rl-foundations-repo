"""
utils/__init__.py
=================
Modules, in curriculum order:

    utils.toy_mdp       GridWorld, tabular policies/values, SARSA, Q-learning, REINFORCE
    utils.ppo           neural policy/value and the clipped-surrogate PPO loop
    utils.reward_model  Bradley-Terry reward model and synthetic preferences (also used in RLHF)
    utils.train         plotting and training helpers
    utils.env           repo root and device
"""

from .env import ENV

__all__ = ["ENV"]
