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

    model_config = ConfigDict(arbitrary_types_allowed=True) # Adding this line to allow Pydantic to recognise pendulum methods as types where necessary


class LogEntry(BaseModel):
    """Pydantic model representing a processed log entry ready for output."""

    start_time: pendulum.Time | None = None
    end_time: pendulum.Time | None = None
    job_description: str | None = None
    log_id: int
    
    @property
    def duration(self) -> pendulum.Duration | None:
        """Calculate the duration between start and end times dynamically."""
        if all([self.start_time, self.end_time]):
            
            start_dt = pendulum.datetime(
                2025,
                6,
                29,  # Assuming a fixed date since logo entries do not include a date
                self.start_time.hour,
                self.start_time.minute,
                self.start_time.second,
            )
            end_dt = pendulum.datetime(
                2025,
                6,
                29,  # Same assumption of a fixed date since log entries do not include a date
                self.end_time.hour,
                self.end_time.minute,
                self.end_time.second,
            )

            return end_dt - start_dt
        return None
    threshold_indicator: ThresholdIndicatorTtype | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
