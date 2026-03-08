from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.middleware.auth_middleware import get_current_user
from app.services.ml_service import predict_yield, detect_price_anomaly

router = APIRouter(prefix="/ml", tags=["ML"])


class YieldRequest(BaseModel):

    area_acres: float
    rainfall: float
    temperature: float


class PriceRequest(BaseModel):

    price: float


@router.post("/predict-yield")
def predict_crop_yield(
    data: YieldRequest,
    user=Depends(get_current_user)
):

    prediction = predict_yield(
        data.area_acres,
        data.rainfall,
        data.temperature
    )

    return {
        "predicted_yield_quintals": prediction
    }


@router.post("/price-anomaly")
def price_anomaly(
    data: PriceRequest,
    user=Depends(get_current_user)
):

    result = detect_price_anomaly(data.price)

    return result