from fastapi import FastAPI

from routers import user_router

app = FastAPI(title="API Users")

app.include_router(user_router)
