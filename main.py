
from fastapi import FastAPI
from api.routes import payment

app = FastAPI(title="CyberSource Payment Gateway")

app.include_router(payment.router, prefix="/api/payment")