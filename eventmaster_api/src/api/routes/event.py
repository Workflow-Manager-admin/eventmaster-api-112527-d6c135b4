from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models import Event
from ..repositories import EventRepository


router = APIRouter(prefix="/events", tags=["Events"])
event_repo = EventRepository()


# PUBLIC_INTERFACE
@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(event: Event):
    """Create a new event."""
    return event_repo.create(event)


# PUBLIC_INTERFACE
@router.get("/", response_model=List[Event])
def list_events():
    """List all events."""
    return event_repo.list()


# PUBLIC_INTERFACE
@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int):
    """Get details of a single event."""
    event = event_repo.get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


# PUBLIC_INTERFACE
@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, event: Event):
    """Update an existing event."""
    updated = event_repo.update(event_id, event)
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated


# PUBLIC_INTERFACE
@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int):
    """Delete an event."""
    success = event_repo.delete(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
