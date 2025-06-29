"""Pydantic models representing log entries.

These models are used to validate and parse log entries from the input log file and generate output logs.
"""

from enum import Enum
from pydantic import BaseModel, ConfigDict
import pendulum


class ThresholdIndicatorTtype(str, Enum):
    """Enum representing the type of threshold indicator."""

    WARNING = "WARNING"
    ERROR = "ERROR"


class LogEntryType(str, Enum):
    """Enum representing the type of log entry."""

    START = "START"
    END = "END"


class RawLogEntry(BaseModel):
    """Pydantic model representing a log entry from the provided log file."""

    timestamp: pendulum.Time
    job_description: str
    log_entry_type: LogEntryType
    pid: int

    model_config = ConfigDict(arbitrary_types_allowed=True) # Adding this line to allow Pydantic to recognise pendulum.Time as a type
