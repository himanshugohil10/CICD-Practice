from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This is your man speaking!"}

@app.get("/health")
def health():
    return {"status": "ok"}
