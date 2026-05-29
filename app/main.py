from fastapi import FastAPI
from app.db.database import Base
from app.router.routers import router
from app.db.database import engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)