import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    count = 1
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for i in range(5):
            response = f"{count} Сообщение пользователя: {message} "
            count += 1
            await websocket.send(response)


# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())
