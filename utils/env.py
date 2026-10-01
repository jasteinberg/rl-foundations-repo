"""
utils/env.py
============
Repo root and device, resolved at import time. Notebooks find the repo
root themselves and then import this:

    from utils.env import ENV
    ENV.summary()
"""

import os
from dataclasses import dataclass

import torch

# Repo root resolved from this file's location (no hardcoded user paths).
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@dataclass(frozen=True)
class _Env:
    REPO      : str = _REPO_ROOT
    NOTEBOOKS : str = os.path.join(_REPO_ROOT, "notebooks")
    DOCS      : str = os.path.join(_REPO_ROOT, "docs")
    DEVICE    : str = (
        "cuda" if torch.cuda.is_available()
        else "mps" if torch.backends.mps.is_available()
        else "cpu"
    )

    def summary(self) -> None:
        print(f"Device:    {self.DEVICE}")
        print(f"Repo:      {self.REPO}")


ENV = _Env()
