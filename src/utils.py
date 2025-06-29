from src.log_model import RawLogEntry, LogEntryType, LogMessage
from loguru import logger
import pendulum

def parse_uploaded_log_file_contents(file_contents:str) -> list[RawLogEntry]:
    """Parse the contents of an uploaded log file.

    This function takes the raw contents of a log file and parses them into the RawLogEntry model for validation and further processing.
    It outputs a list of RawLogEntry instances, each representing a single log entry for subsequent processing.

    Args:
        file_contents (str): The raw contents of the uploaded log file.

    Returns:
        list[RawLogEntry]: A list of parsed log entries.
    """

    entries = []
    
    lines = file_contents.strip().splitlines()
    for line in lines:
        values = [v.strip() for v in line.split(",")]
        if len(values) != 4:
            logger.error(f"Invalid log entry format: {line}")
            continue
        try:
            entry = RawLogEntry(
                timestamp=pendulum.parse(values[0]).time(),
                job_description=values[1],
                log_entry_type=values[2],
                pid=int(values[3])
            )
            entries.append(entry)
        except Exception as e:
            logger.error(f"Error parsing log entry: {line}, Error: {e}")
            continue

    return entries

def extract_continuous_log_entries(file_contents) -> dict[int, LogMessage]:
    """Extract continuous log entries from the provided file contents.

    This function processes the raw log entries and extracts continuous log entries based on their start and end times.
    It returns a dictionary mapping job IDs to their respective continuous log entries.

    Args:
        file_contents (str): The raw contents of the uploaded log file.

    Returns:
        dict[int, LogMessage]: A dictionary mapping job IDs to their respective continuous log entries.
    """
    
    return {}