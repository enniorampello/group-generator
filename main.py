from telethon import TelegramClient
from telethon.tl import functions
from telethon.client.chats import ChatMethods
from telethon.events.newmessage import NewMessage
import asyncio
from time import sleep

with open('./api.txt', 'r') as keys:
    api_id = int(keys.readline())
    api_hash = keys.readline()

default_msg = 'Hi! This message has been sent (again) through the Telegram Api.'
group_help_bot_username = 'GroupHelpBot'
add_bot_command = '/start@GroupHelpOfficialClone3Bot'


async def main():
    async with TelegramClient('groupgen', api_id, api_hash) as client:
        channel_name = 'third group'
        result = await client(functions.channels.CreateChannelRequest(
            title=channel_name,
            about='This group has been created through the Telegram API',
            megagroup=True,
        ))
        channel_id = result.updates[1].channel_id
        await ChatMethods.edit_permissions(
            client,
            channel_id,
            change_info=False,
            pin_messages=False
        )

        await client.send_message(
            channel_id,
            add_bot_command
        )

        NewMessage(
            channel_id,
            incoming=True,
            outgoing=False,
            from_users=group_help_bot_username,
            func= add_bot(client, channel_id)
        )

        await ChatMethods.edit_admin(
            client,
            channel_id,
            group_help_bot_username,
            is_admin=True
        )

        sleep(60)

        await client(functions.channels.DeleteChannelRequest(
            channel_id
        ))

async def add_bot(client, channel_id):
    return await client.send_message(
        channel_id,
        add_bot_command
    )

if __name__ == '__main__':
    asyncio.run(main())



'''
third course,157684
fourth course,321321
fifth course,789456
sixth course,654963
seventh course,357951
'''
