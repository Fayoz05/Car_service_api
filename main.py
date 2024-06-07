from fastapi import FastAPI
from database import Base, engine
from API.car_service_api.car_service import service_router


# uvicorn main:app --reload для запуска
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')
app.include_router(service_router)