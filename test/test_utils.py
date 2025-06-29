import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import (
    parse_uploaded_log_file_contents,
    extract_continuous_log_entries,
)
from src.log_model import RawLogEntry, LogEntryType, LogMessage


def test_parse_uploaded_log_file_contents():
    """Test the parse_uploaded_log_file_contents function."""
    file_contents = """
    12:00:00, Job A, START, 1234
    12:05:00, Job A, END, 1234
    12:10:00, Job B, START, 5678
    12:15:00, Job B, END, 5678
    """
    entries = parse_uploaded_log_file_contents(file_contents)
    assert len(entries) == 4
    assert isinstance(entries[0], RawLogEntry)
    assert entries[0].log_entry_type == LogEntryType.START
    assert entries[1].log_entry_type == LogEntryType.END
    assert entries[2].pid == 5678
    assert entries[3].job_description == "Job B"
    assert entries[2].timestamp.hour == 12
    assert entries[3].timestamp.minute == 15
    
def test_extract_continuous_log_entries():
    """Test the extract_continuous_log_entries function."""
    file_contents = """
    12:00:00, Job A, START, 1234
    12:05:00, Job A, END, 1234
    12:10:00, Job B, START, 5678
    12:15:00, Job B, END, 5678
    """
    continuous_entries = extract_continuous_log_entries(file_contents)
    
    assert len(continuous_entries) == 2
    assert isinstance(continuous_entries[1234], LogMessage)
    assert continuous_entries[1234].start_time is not None
    assert continuous_entries[1234].job_description == "Job A"
    assert continuous_entries[5678].job_description == "Job B"
    assert continuous_entries[1234].start_time.hour == 12
    assert continuous_entries[5678].end_time.minute == 15