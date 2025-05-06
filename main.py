
from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="CyberSource Payment Gateway")

app.include_router(router)