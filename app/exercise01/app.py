from fastapi import FastAPI, status

app = FastAPI()


messages = {"message_00": "Hello, World!"}

@app.get("/")
def get_messages():
    return messages

@app.post("/message", status_code=status.HTTP_201_CREATED)
def create_message(message: str):
    currently_index = len(messages) + 1 
    next_key_index = f"message_{currently_index}"
    messages[next_key_index] = message
    return f"Message number {currently_index} Created!"

@app.put("/message/{id}")
def update_message(id: int, message: str):
    this_key = f"message_{id}"
    messages.update(this_key + ":" + message)
    return f"Message number {id} Updated!"

@app.delete("/message/{id}")
def delete_message(id: int):
    messages.pop(id)
    return f"Message number {id} Deleted!"
