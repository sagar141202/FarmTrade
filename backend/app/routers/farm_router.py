from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.farm import Farm
from app.schemas.farm_schema import FarmCreate, FarmResponse
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter(prefix="/farms", tags=["Farms"])


@router.post("/create", response_model=FarmResponse)
def create_farm(
    farm: FarmCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_farm = Farm(
        user_id=current_user.id,
        name=farm.name,
        location=farm.location,
        area_acres=farm.area_acres,
        soil_type=farm.soil_type,
        irrigation_type=farm.irrigation_type,
        lat=farm.lat,
        lng=farm.lng
    )

    db.add(new_farm)
    db.commit()
    db.refresh(new_farm)

    return new_farm


@router.get("/my-farms")
def get_my_farms(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    farms = db.query(Farm).filter(Farm.user_id == current_user.id).all()

    return farms
