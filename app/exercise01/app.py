from fastapi import FastAPI, HTTPException, status

app = FastAPI()


messages = {"message_0": "Hello, World!"}


@app.get("/")
def get_messages():
    if not messages:
        raise HTTPException(status_code=404, detail="No message found!")
    
    return messages


@app.post("/message", status_code=status.HTTP_201_CREATED)
def create_message(message: str):
    current_index = len(messages) + 1
    next_key_index = f"message_{current_index}"
    messages[next_key_index] = message
    
    return f"Message number {current_index} Created!"


@app.put("/message/{id}")
def update_message(id: int, message: str):
    this_key = f"message_{id}"

    if not this_key in messages:
        raise HTTPException(status_code=404, detail=f"The message number {id} doesn't exists!")
    
    messages.update({this_key: message})
    return f"Message number {id} Updated!"


@app.delete("/message/{id}")
def delete_message(id: int):
    this_key = f"message_{id}"

    if not this_key in messages:
        raise HTTPException(status_code=404, detail=f"The message number {id} doesn't exists. So it cannot be deleted!")
    
    messages.pop(this_key)
    return f"Message number {id} Deleted!"
