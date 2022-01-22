import websockets
import asyncio


class Producer:
    def __init__(self, host:str, port:str)-> None:
        self.url = f"ws://{host}:{port}/ws"

    async def produce(self, message):
        async with websockets.connect(self.url) as ws:
            await ws.send(message)
            data = await ws.recv()
            print(data)
        

if __name__ == '__main__':
    producer = Producer('127.0.0.1', '8089')
    asyncio.run(producer.produce(message='passsssha'))
    # loop = asyncio.get_event_loop()
    
    # loop.run_forever()