from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.event import router as event_router
from .routes.attendee import router as attendee_router
from .routes.schedule import router as schedule_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_router)
app.include_router(attendee_router)
app.include_router(schedule_router)


@app.get("/")
def health_check():
    return {"message": "Healthy"}
