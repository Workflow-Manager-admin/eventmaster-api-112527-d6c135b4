# In-memory repositories for demo and development purposes.
from typing import List, Optional, Dict
from .models import Event, Attendee, Schedule


class EventRepository:
    def __init__(self):
        self.events: Dict[int, Event] = {}
        self.next_id = 1

    # PUBLIC_INTERFACE
    def create(self, event: Event) -> Event:
        event.id = self.next_id
        self.next_id += 1
        self.events[event.id] = event
        return event

    # PUBLIC_INTERFACE
    def get(self, event_id: int) -> Optional[Event]:
        return self.events.get(event_id)

    # PUBLIC_INTERFACE
    def list(self) -> List[Event]:
        return list(self.events.values())

    # PUBLIC_INTERFACE
    def update(self, event_id: int, new_event: Event) -> Optional[Event]:
        if event_id in self.events:
            updated_event = new_event.copy()
            updated_event.id = event_id
            self.events[event_id] = updated_event
            return updated_event
        return None

    # PUBLIC_INTERFACE
    def delete(self, event_id: int) -> bool:
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False


class AttendeeRepository:
    def __init__(self):
        self.attendees: Dict[int, Attendee] = {}
        self.next_id = 1

    # PUBLIC_INTERFACE
    def create(self, attendee: Attendee) -> Attendee:
        attendee.id = self.next_id
        self.next_id += 1
        self.attendees[attendee.id] = attendee
        return attendee

    # PUBLIC_INTERFACE
    def get(self, attendee_id: int) -> Optional[Attendee]:
        return self.attendees.get(attendee_id)

    # PUBLIC_INTERFACE
    def list(self) -> List[Attendee]:
        return list(self.attendees.values())

    # PUBLIC_INTERFACE
    def update(self, attendee_id: int, new_attendee: Attendee) -> Optional[Attendee]:
        if attendee_id in self.attendees:
            updated = new_attendee.copy()
            updated.id = attendee_id
            self.attendees[attendee_id] = updated
            return updated
        return None

    # PUBLIC_INTERFACE
    def delete(self, attendee_id: int) -> bool:
        if attendee_id in self.attendees:
            del self.attendees[attendee_id]
            return True
        return False


class ScheduleRepository:
    def __init__(self):
        self.schedules: Dict[int, Schedule] = {}
        self.next_id = 1

    # PUBLIC_INTERFACE
    def create(self, schedule: Schedule) -> Schedule:
        schedule.id = self.next_id
        self.next_id += 1
        self.schedules[schedule.id] = schedule
        return schedule

    # PUBLIC_INTERFACE
    def get(self, schedule_id: int) -> Optional[Schedule]:
        return self.schedules.get(schedule_id)

    # PUBLIC_INTERFACE
    def list(self) -> List[Schedule]:
        return list(self.schedules.values())

    # PUBLIC_INTERFACE
    def update(self, schedule_id: int, new_schedule: Schedule) -> Optional[Schedule]:
        if schedule_id in self.schedules:
            updated = new_schedule.copy()
            updated.id = schedule_id
            self.schedules[schedule_id] = updated
            return updated
        return None

    # PUBLIC_INTERFACE
    def delete(self, schedule_id: int) -> bool:
        if schedule_id in self.schedules:
            del self.schedules[schedule_id]
            return True
        return False
