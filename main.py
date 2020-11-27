from telethon import TelegramClient
from telethon.tl import functions
import asyncio
from keys import get_keys
import pandas as pd


api_id = get_keys()['id']
api_hash = get_keys()['hash']

group_help_bot_username = 'hkbannerbot'

async def main():
    async with TelegramClient('groupgen', api_id, api_hash) as client:
        df = pd.read_csv('courses.csv')
        links = []
        channel_ids = []
        for idx, course in df.iterrows():
            channel_name = course['name']
            course_id = course['id']
            result = await client(functions.channels.CreateChannelRequest(
                title=channel_name,
                about=f'Official group for the course {channel_name} ({course_id}). Provided by HKN Polito.',
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
            channel_link = await client(functions.messages.ExportChatInviteRequest(
                channel_id
                ))
            links.append(channel_link.link)
            await client(functions.messages.SendMessageRequest(
                channel_id,
                '/setgruppostaff -1001145664991',
            ))
        df['channel_id'] = channel_ids
        df['channel_link'] = links
        df.to_csv('courses.csv')


if __name__ == '__main__':
    asyncio.run(main())

'''
hour_count = 21
'''