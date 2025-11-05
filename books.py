from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def first_api():
    return {"message": "hi"}
