from telethon import TelegramClient
import time
#from telethon.sessions import StringSession
from config import (API_ID, API_HASH, SESSION_STRING, CHAT_ID)

#loop = asyncio.get_event_loop()
#if SESSION_STRING:
    #client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
#else:
client = TelegramClient('don', API_ID, API_HASH)
nnn = 1

async def main():
    iii = 1000
    async for message in client.iter_messages(CHAT_ID):
        if 'MessageActionChatAddUser' in str(message.action):
        	await client.delete_messages(CHAT_ID, message.id)
        iii -= 1
        if iii == 0:
        	break
#    await asyncio.sleep(60)

with client:
    while True:
        client.loop.run_until_complete(main())
        print(nnn, ' ')
        nnn += 1
        time.sleep(60)

#loop.run_until_complete(main())
