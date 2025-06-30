# Log Monitoring Application

A FastAPI application that processes log files to calculate job durations, apply threshold indicators to an output log file. The application uses uv by astral for package and dependency management.

## Features

- Parses CSV log files with START/END entries
- Calculates job durations dynamically
- Allows for dynamic application of threshold indicators. Default is currently set to ("WARNING" for duration greater than 5 minutes and "ERROR" when greater than 10 minutes)
- Makes processed results as text files

## Setup
1. Clone and navigate to the project:
   ```bash
   git clone https://github.com/Chukwuedo/log-monitoring-application.git
   cd log-monitoring-appplication
   ```

2. Create and activate a virtual environment
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/macOS
   python -m venv .venv
   source .venv/bin/activate
   ``` 

3. Install dependencies
   ```bash
   uv sync
   ```

## Usage

Run the application
```bash
uvicorn main:app --port 8080 --reload
```


Access the API at [http://localhost:8080/docs](http://localhost:8080/docs)

## API

**GET /**

- Returns a welcome message confirming the API is running.

**GET /health**

- Returns a simple status check indicating the service is healthy.

**POST /process-log-file/**
- Upload a log file with columns entries for timestamp, job_description, log_entry_type, pid. See an example below in the `CSV Format` section of what is expected
    
- Returns a processed text file with durations and threshold indicators. See the log_output file in the repository for an example of what the API will produce

## Testing

```bash
pytest
```

## CSV Format
```
11:35:23,scheduled task 032, START,37980
11:35:56,scheduled task 032, END,37980
11:36:11,scheduled task 796, START,57672
11:36:18,scheduled task 796, END,57672

```