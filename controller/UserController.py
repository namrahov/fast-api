from fastapi import File, Body, status, WebSocket, WebSocketDisconnect, Depends
from main import app
from db.database import db_dependency as db_depenceny, get_session
from service.UserService import *
import json
from model.UserCreateRequest import UserCreateRequest

#https://chatgpt.com/share/6915b05c-08b0-800f-86e7-25c6de459305
@app.websocket("/ws/upload-excel")
async def upload_excel_socket(websocket: WebSocket,
                              db: db_depenceny = None):

    await websocket.accept()
    user_service = UserService(db)

    try:
        while True:
            message = await websocket.receive()

            # -----------------------
            # TEXT MESSAGES
            # -----------------------
            if "text" in message:
                data = json.loads(message["text"])
                msg_type = data["type"]

                if msg_type == "start":
                    user_service.start_upload(data)
                    await websocket.send_text("START_OK")

                elif msg_type == "end":
                    count = user_service.finish_upload()
                    await websocket.send_text(f"UPLOAD_COMPLETED: {count} users")
                    break

            # -----------------------
            # BINARY CHUNKS
            # -----------------------
            elif "bytes" in message:
                chunk = message["bytes"]
                size = user_service.append_chunk(chunk)
                await websocket.send_text(f"CHUNK_OK:{size}")

    except WebSocketDisconnect:
        print("Client disconnected unexpectedly")


@app.post("/upload-excel", status_code=status.HTTP_201_CREATED)
async def upload_excel(file: UploadFile = File(...), db: db_depenceny = None):
    await UserService(db).upload_excel_file(file)


#Oxuduqca db-yƏ yaz
@app.post("/upload-excel-stream")
async def upload_excel_stream(
        file: UploadFile = File(...),
        db: db_depenceny = None
):
    result = await UserService(db).save_excel_stream(file)
    return result

@app.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: UserCreateRequest = Body(...), db: Session = Depends(get_session)):
    await UserService(db).create_user(create_user_request)