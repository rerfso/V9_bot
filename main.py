from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/chat")
def chat(data: dict):
    text = data.get("text", "")

    return {
        "response": f"Ты написал: {text}"
