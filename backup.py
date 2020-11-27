import asyncio
from telethon import TelegramClient
from telethon.tl import functions
from keys import get_keys
import pandas as pd

api_id = get_keys()['id']
api_hash = get_keys()['hash']

async def main():
    async with TelegramClient('groupgen', api_id, api_hash) as client:
        df = pd.read_csv('courses.csv')
        for idx, channel in df.iterrows():
            id = channel['channel_id']
            await client.send_file(
                id,
                file='backimport.jpg',
                caption='.backimport'
            )

if __name__ == '__main__':
    asyncio.run(main())