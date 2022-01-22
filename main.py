from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from fastapi.staticfiles import StaticFiles
from mainapp.api_routes import router
from mainapp.html_routes import html_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            await websocket.send_text('qwqwqwqwqw')
    except WebSocketDisconnect:
        print('disconnected')
        


app.include_router(router)
app.include_router(html_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8089)