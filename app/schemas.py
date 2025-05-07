# schemas.py
from pydantic import BaseModel, Field

#constr -> brought error: call expression not allowed in type expression so instead used Field

#class CardInfo(BaseModel):
#    number: constr(min_length=13, max_length=19) 
#    expirationMonth: constr(min_length=1, max_length=2)
#    expirationYear: constr(min_length=4, max_length=4)
#    securityCode: constr(min_length=3, max_length=4)

class CardInfo(BaseModel):
    number: str = Field(min_length=13, max_length=19)
    expirationMonth: str = Field(min_length=1, max_length=2)
    expirationYear: str = Field(min_length=4, max_length=4)
    securityCode: str = Field(min_length=3, max_length=4)

class PaymentInfo(BaseModel):
    card: CardInfo

class AmountDetails(BaseModel):
    totalAmount: str
    currency: str

class BillTo(BaseModel):
    firstName: str
    lastName: str
    address1: str
    email: str
    phoneNumber: str
    country: str

class OrderInformation(BaseModel):
    amountDetails: AmountDetails
    billToInfo: BillTo

class ProcessInformation(BaseModel):
    capture: bool

class PaymentRequest(BaseModel):
    clientReferenceInformation: dict
    processingInformation: dict
    paymentInformation: dict
    orderInformation: dict

class PaymentResponse(BaseModel):
    status: str
    id: str
    clientReferenceInformation: dict
