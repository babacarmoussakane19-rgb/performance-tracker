from fastapi import FastAPI

app = FastAPI(
    title="Personal Performance Tracker API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Personal Performance Tracker API",
        "status": "running"
    }