# Log Monitoring Application

A FastAPI application that processes log files to calculate job durations, apply threshold indicators to an output log file. The application uses uv by astral for package and dependency management.

## Features

- Parses CSV-structured log files (without the headers) with START/END entries
- Calculates job durations dynamically
- Allows for dynamic application of threshold indicators. Default is currently set to ("WARNING" for duration greater than 5 minutes and "ERROR" when greater than 10 minutes)
- Makes processed results as text files

## Requirements
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management

## Setup
1. Clone and navigate to the project:
   ```bash
   git clone https://github.com/Chukwuedo/log-monitoring-application.git
   cd log-monitoring-application
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

## Project Structure

```
log-monitoring-application/
├── main.py             # FastAPI application entry point
├── src/
│   ├── log_model.py    # Pydantic models for log entries
│   └── utils.py        # Log processing utilities
├── test/
│   └── test_utils.py   # Unit tests
├── README.md
└── ...
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

Ensure you have activated the virtual environment before running the tests. Once done, run the command below

```bash
pytest
```

## CSV Format

The uploaded log file should be a CSV format but does not have to have the .csv extension. The entry should have the following columns (no header required):
`timestamp, job_description, log_entry_type, pid`

```
11:35:23,scheduled task 032, START,37980
11:35:56,scheduled task 032, END,37980
11:36:11,scheduled task 796, START,57672
11:36:18,scheduled task 796, END,57672
```

## Example Usage
There are two ways to use the API:
1. By trying it out through the Swagger UI accessible at [http://localhost:8080/docs](http://localhost:8080/docs)
   - First locate the `POST /process-log-file/` endpoint and then click on the `Try it out` button
   - Next, click on the `Choose File` button to upload the log file and then click on the blue `Execute` button
   - In the `Responses` section look for the `Download File` link and receive the processed log
2. By uploading a log file using curl using the example below:
    ```bash
    curl -F "file=@logs 9.log" http://localhost:8080/process-log-file/
    ```
    This approach will output the processed logs directly in terminal


## Error Handling & Limitations

- The API validates each log entry using strict Pydantic models. Invalid or malformed entries are automatically skipped and logged as errors using the built-in logger.
- If a log entry has an invalid format or an unrecognized entry type, it will not be included in the processed output. These issues are recorded in the application logs for review.
- The API expects log files to follow the described CSV format. Files that deviate significantly from this format may result in no output or incomplete processing.
- No error details are returned in the API response for security and simplicity; all error information is available in the server logs.


## What I Would Do With More Time

- **Expand Test Coverage:** Add more comprehensive unit and integration tests using the `hypothesis` library, including edge cases and malformed input scenarios, to ensure robustness. Also, I could explore load/performance testing with `locust` to assure reliability. 
- **Improve Error Reporting:** Enhance error handling to provide more detailed feedback to users through the API, and return structured error responses with Pydantic.
- **Performance Optimisation:** Profile and optimise the log processing for very large files or concurrent uploads using lighter and more performant data structures.
- **Configuration Options:** Allow users to customise threshold values (for warnings and errors) through environment variables or API parameters.
- **User Interface:** Build a simple web UI using htmx and alpinejs for uploading log files and viewing results directly in the browser.
- **Deployment:** Add a Dockerfile and deployment instructions for easier setup in different environments e.g. distributed systems.
- **API Enhancements:** Provide additional endpoints for querying processed logs or job statistics for continuous API improvement.