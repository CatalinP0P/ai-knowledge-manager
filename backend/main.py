from fastapi import FastAPI

app = FastAPI(title="AI Knowledge Manager API")

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Ready to process courses!"}
