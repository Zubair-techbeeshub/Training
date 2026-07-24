from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str
    tags: list[str]

NOTES = []

def find_note(note_id: str):
    note = next((n for n in NOTES if n["id"] == note_id),None)
    if note is None: raise HTTPException(status_code=404,detail="Note not found")
    return note

@app.post("/notes")
async def create_note(note: Note):
    new_note = {
        "id": str(uuid4()),
        **note.model_dump(),
        "created_at": datetime.now().isoformat()
    }
    NOTES.append(new_note)
    return new_note

@app.get("/notes")
async def get_notes():
    return NOTES

@app.get("/notes/search")
async def search_notes(tag: str):
    filtered_notes = [note for note in NOTES if tag in note["tags"]]
    return filtered_notes

@app.get("/notes/{note_id}")
async def get_note(note_id: str):
    return find_note(note_id)


@app.put("/notes/{note_id}")
async def update_note(note_id: str, updated_note: Note):
    note = find_note(note_id)
    note["title"] = updated_note.title
    note["content"] = updated_note.content
    note["tags"] = updated_note.tags
    note["updated_at"] = datetime.now().isoformat()
    return note

@app.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    note = find_note(note_id)
    NOTES.remove(note)
    return {"message": "Note deleted successfully"}

