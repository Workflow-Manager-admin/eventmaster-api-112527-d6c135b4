from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models import Attendee
from ..repositories import AttendeeRepository


router = APIRouter(prefix="/attendees", tags=["Attendees"])
attendee_repo = AttendeeRepository()


# PUBLIC_INTERFACE
@router.post("/", response_model=Attendee, status_code=status.HTTP_201_CREATED)
def create_attendee(attendee: Attendee):
    """Create a new attendee."""
    return attendee_repo.create(attendee)


# PUBLIC_INTERFACE
@router.get("/", response_model=List[Attendee])
def list_attendees():
    """List all attendees."""
    return attendee_repo.list()


# PUBLIC_INTERFACE
@router.get("/{attendee_id}", response_model=Attendee)
def get_attendee(attendee_id: int):
    """Get a single attendee."""
    attendee = attendee_repo.get(attendee_id)
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    return attendee


# PUBLIC_INTERFACE
@router.put("/{attendee_id}", response_model=Attendee)
def update_attendee(attendee_id: int, attendee: Attendee):
    """Update attendee details."""
    updated = attendee_repo.update(attendee_id, attendee)
    if not updated:
        raise HTTPException(status_code=404, detail="Attendee not found")
    return updated


# PUBLIC_INTERFACE
@router.delete("/{attendee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attendee(attendee_id: int):
    """Delete an attendee."""
    success = attendee_repo.delete(attendee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Attendee not found")
