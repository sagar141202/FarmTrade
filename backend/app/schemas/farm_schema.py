from pydantic import BaseModel


class FarmCreate(BaseModel):
    name: str
    location: str
    area_acres: float
    soil_type: str
    irrigation_type: str
    lat: float
    lng: float


class FarmResponse(BaseModel):
    id: int
    name: str
    location: str
    area_acres: float
    soil_type: str
    irrigation_type: str
    lat: float
    lng: float

    class Config:
        from_attributes = True
