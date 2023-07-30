from fastapi import FastAPI
from financial.routers import router


app = FastAPI()
app.include_router(router)


@app.get("/")
def healthy_check():
    return "I am alive"

