from fastapi import APIRouter, HTTPException
from app.service.charge import ChargeFunc
from app.schemas import PaymentRequest, PaymentResponse

router = APIRouter()
charge_function = ChargeFunc()

@router.post("/payment", response_model=PaymentResponse)
def charge_card(request: PaymentRequest):
    try:
        response = charge_function.charge_card(
            amount=request.amount,
            currency=request.currency,
            card_details=request.card_details,
            billing_info=request.bill_info
        )
        return response
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )