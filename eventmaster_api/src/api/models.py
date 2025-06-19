# Data models for the EventMaster API-112527 backend.
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


# PUBLIC_INTERFACE
class Schedule(BaseModel):
    """Represents a schedule item for an event."""
    id: int = Field(..., example=1)
    title: str = Field(..., example="Opening Ceremony")
    start_time: datetime
    end_time: datetime
    description: Optional[str] = None


# PUBLIC_INTERFACE
class Attendee(BaseModel):
    """Represents an attendee."""
    id: int = Field(..., example=1)
    name: str = Field(..., example="Alice Smith")
    email: str = Field(..., example="alice@example.com")


# PUBLIC_INTERFACE
class Event(BaseModel):
    """Represents an event."""
    id: int = Field(..., example=1)
    name: str = Field(..., example="Tech Conference 2024")
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    attendees: List[Attendee] = []
    schedules: List[Schedule] = []
