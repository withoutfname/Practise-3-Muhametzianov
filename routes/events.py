
from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from database.connection import Database
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events():
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId):
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


@event_router.post("/new")
async def create_event(event: Event) -> dict:
    await event_database.save(event)
    return {"message": "Event created successfully"}


@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate):
    updated = await event_database.update(id, body)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    deleted = await event_database.delete(id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {"message": "Event deleted successfully."}