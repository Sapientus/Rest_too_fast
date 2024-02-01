from fastapi import FastAPI
import uvicorn
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api")


@app.get("/")
def read_root():
    return {
        "message": "Did you know that in the reality everything is different than it actually is"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
