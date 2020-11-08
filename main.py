from telethon import TelegramClient
from telethon.tl import functions
import asyncio
from keys import get_keys


api_id = get_keys()['id']
api_hash = get_keys()['hash']

group_help_bot_username = 'GroupHelpOfficialClone2Bot'
channel_ids = []

async def main():
    async with TelegramClient('groupgen', api_id, api_hash) as client:
        channel_name = 'test channel'
        result = await client(functions.channels.CreateChannelRequest(
            title=channel_name,
            about='This group has been created through the Telegram API',
            megagroup=True,
        ))
        channel_id = result.updates[1].channel_id
        channel_ids.append(channel_id)
        result = await client(functions.channels.InviteToChannelRequest(
            channel_id, 
            [group_help_bot_username]
            ))
        await client.edit_admin(
            channel_id,
            group_help_bot_username,
            is_admin=True,
            title='spam god'
        )


if __name__ == '__main__':
    asyncio.run(main())

'''
hour_count = 3g
'''