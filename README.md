# rl-foundations

<!-- [JS: introduction to write: audience, what the curriculum covers, how it is meant to be read] -->

## Contents

| Step | Notebook | Library code | Notes |
|---|---|---|---|
| 1. Tabular control: SARSA, Q-learning, Monte Carlo | `notebooks/tabular_control/` | `utils/toy_mdp.py` | |
| 2. Policy gradients: REINFORCE | `notebooks/policy_gradient/` | `utils/toy_mdp.py` | `docs/policy_gradient.md` |
| 3. PPO: the clipped surrogate | `notebooks/ppo/` | `utils/ppo.py` | `docs/ppo.md` |
| 4. Reward modelling: Bradley–Terry | `notebooks/reward_modeling/` | `utils/reward_model.py` | |
| 5. RLHF: the KL-regularised objective | `notebooks/rlhf_pipeline/` | `utils/reward_model.py` | |

## Running

```bash
pip install -r requirements.txt
jupyter lab
```

Each notebook finds the repo root by walking up from its own directory, so it runs from wherever the repo is checked out.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
