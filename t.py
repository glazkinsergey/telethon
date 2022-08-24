from telethon import TelegramClient
import time
from telethon.sessions import StringSession
from config import (API_ID, API_HASH, SESSION_STRING, CHAT_ID)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
nnn = 1

async def main():
    iii = 1000
    async for message in client.iter_messages(CHAT_ID):
        if 'MessageActionChatAddUser' in str(message.action):
        	await client.delete_messages(CHAT_ID, message.id)
        iii -= 1
        if iii == 0:
        	break

with client:
    while True:
        client.loop.run_until_complete(main())
        print(nnn, ' ')
        nnn += 1
        
        tim = time.localtime()
        current_time = time.strftime("%H", tim)
        
        if current_time == 1:
            time.sleep(21600)
            print(nnn, ' SLEEPING 6 hours. Economy DynoHours. ')
        else:
            time.sleep(60)
