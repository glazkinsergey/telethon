from telethon import TelegramClient
import time
from config import (API_ID, API_HASH, SESSION_STRING)

#loop = asyncio.get_event_loop()

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
nnn = 1

async def main():
    iii = 1000
    async for message in client.iter_messages('dprpetrovka'):
        if 'MessageActionChatAddUser' in str(message.action):
        	await client.delete_messages('dprpetrovka', message.id)
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
