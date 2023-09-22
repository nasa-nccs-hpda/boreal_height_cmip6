from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """
    CNN data configuration class (embedded with OmegaConf).
    """

    # Directory to store all data files
    input_dir: str = "."

    # Directory to store model artifacts
    output_dir: Optional[str] = "."

    # String with action to perform
    action: str = "run"
