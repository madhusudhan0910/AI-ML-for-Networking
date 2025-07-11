from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import redis
import json
from app.predict import detect_threat
app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
r = redis.Redis(host="redis", port=6379, db=0)
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("frontend/index.html") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Frontend not found")
@app.post("/detect/")
async def detect(payload: str = Form(...)):
    if not payload.strip():
        raise HTTPException(status_code=400, detail="Payload cannot be empty")
    result = detect_threat(payload)
    r.rpush("threat_queue", json.dumps({
        "type": "single",
        "payload": payload,
        "result": result
    }))
    return {"result": result}
@app.post("/detect_file/")
async def detect_file(file: UploadFile = File(...)):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="File cannot be empty")
    try:
        lines = content.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Unable to decode file. Please upload UTF-8 encoded text file."
        )
    results = []
    for line in lines:
        clean_line = line.strip()
        if clean_line:
            label = detect_threat(clean_line)
            results.append({"payload": clean_line, "result": label})
    r.rpush("threat_queue", json.dumps({
        "type": "file",
        "file": file.filename,
        "results": results
    }))
    return {"filename": file.filename, "results": results}
