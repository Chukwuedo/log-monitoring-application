from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from src.utils import write_out_proper_log_file
import io
import pendulum

app = FastAPI(title="Log Monitoring Application", description="An application that takes in a provided log file and processes it so it can be monitored for performance issues.")

@app.get("/")
async def root():
    return {"message": "Welcome to the Log Monitoring Application API."}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/process-log-file/")
async def process_log_file(file: UploadFile = File(...)):
    contents = (await file.read()).decode("utf-8")
    processed_logs = write_out_proper_log_file(contents)
    return_file = io.StringIO(processed_logs)
    timestamp = pendulum.now("UTC").format("YYYYMMDDHHmmss")
    output_filename = f"{timestamp}_log_output.txt"
    
    return StreamingResponse(
        return_file,
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={output_filename}"},
    )