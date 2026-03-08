# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base

from app.routers.auth_router import router as auth_router

# import models so SQLAlchemy registers them
from app.models.user import User
from app.models.farm import Farm
from app.models.crop import Crop
from app.models.proposal import Proposal
from app.models.investment import Investment
from app.models.price_report import PriceReport


app = FastAPI(
    title="CropChain API",
    version="1.0"
)

origins = [
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register routers
app.include_router(auth_router)

# create tables in database
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "CropChain API running"}


@app.get("/health")
def health():
    return {"status": "healthy"}