
from fastapi import FastAPI

from app.api.loop_test import router


app =FastAPI()

app.include_router(router)


