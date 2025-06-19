from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models import Schedule
from ..repositories import ScheduleRepository


router = APIRouter(prefix="/schedules", tags=["Schedules"])
schedule_repo = ScheduleRepository()


# PUBLIC_INTERFACE
@router.post("/", response_model=Schedule, status_code=status.HTTP_201_CREATED)
def create_schedule(schedule: Schedule):
    """Create a new schedule."""
    return schedule_repo.create(schedule)


# PUBLIC_INTERFACE
@router.get("/", response_model=List[Schedule])
def list_schedules():
    """List all schedules."""
    return schedule_repo.list()


# PUBLIC_INTERFACE
@router.get("/{schedule_id}", response_model=Schedule)
def get_schedule(schedule_id: int):
    """Get a single schedule entry."""
    schedule = schedule_repo.get(schedule_id)
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


# PUBLIC_INTERFACE
@router.put("/{schedule_id}", response_model=Schedule)
def update_schedule(schedule_id: int, schedule: Schedule):
    """Update an existing schedule entry."""
    updated = schedule_repo.update(schedule_id, schedule)
    if not updated:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated


# PUBLIC_INTERFACE
@router.delete("/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule(schedule_id: int):
    """Delete a schedule entry."""
    success = schedule_repo.delete(schedule_id)
    if not success:
        raise HTTPException(status_code=404, detail="Schedule not found")
