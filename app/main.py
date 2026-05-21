from fastapi import FastAPI
from app.api.v1.devices import router as device_router
from app.api.v1.users import router as user_router
import uvicorn

app = FastAPI()


app.include_router(device_router)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)