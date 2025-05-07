# define api endpoints

from fastapi import APIRouter, HTTPException
from client.cybersource_client import CyberSourceClient
from app.schemas import PaymentRequest, PaymentResponse

router = APIRouter()
cybersource = CyberSourceClient()

# api endpoints
@router.post("/pay", response_model=PaymentResponse)
# make payment api endpoint
async def make_payment(payment: PaymentRequest):
    try:
        result = await cybersource.charge_card() #payment.dict() is deprecated # you can go manual instead if you dont want to work with the SDK
        if "status" in result and result["status"] == "AUTHORIZED":
            return result
        else:
            raise HTTPException(status_code=400, detail=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

