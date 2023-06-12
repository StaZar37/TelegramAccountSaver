

from config import *

from telethon import TelegramClient, events
from telethon.sync import TelegramClient as TC

import sys

try:
	phone = sys.argv[1]
except:
	exit()

# client = TC(f"accs/{phone}/{phone}.session", api_id, api_hash)
# client.send_message("me", "Script TAS is working rn. . .")
# client.start()
# del(client)

client = TelegramClient(f"accs/{phone}/{phone}.session", api_id, api_hash)

@client.on(events.NewMessage)
async def get_msg(e):
	try:
		id = e.message.peer_id.user_id
		if id == 777000:
			msg = e.message.message
			print(msg)
			if "Код подтверждения:" in msg:
				code = msg.split(" ")[2].replace(".", "")

				import datetime
				name = str(datetime.datetime.now().timestamp()).split(".")[0]

				open(f"codes/{name}.txt", "w", encoding="utf8").write(f"{phone}:{code}")
	except:
		pass

client.start()
client.send_message("me", "Script TAS is working rn. . .")
client.run_until_disconnected()