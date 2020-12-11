import asyncio
import pygazebo


def cb(data):
    message = pygazebo.msg.gz_string_pb2.GzString.FromString(data)
    print('Received message:', message.data)

async def publish_loop():
    manager = await pygazebo.connect()

    publisher = await manager.advertise(
        '/joint/cmd',
        'gazebo.msgs.GzString')
    
    message = pygazebo.msg.gz_string_pb2.GzString()
    message.data = "3.14"
    
    while True:
        await publisher.publish(message)
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(publish_loop())