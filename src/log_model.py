"""Pydantic models representing log entries.

These models are used to validate and parse log entries from the input log file and generate output logs.
"""

from enum import Enum
from pydantic import BaseModel


class ThresholdIndicatorTtype(str, Enum):
    """Enum representing the type of threshold indicator."""

    WARNING = "WARNING"
    ERROR = "ERROR"