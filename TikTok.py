from pyrogram import Client,filters
from pyrogram.types import Message
from ..utils.utils import modules_help,prefix
import requests
import json

@Client.on_message(filters.command("tt",prefix) & filters.me)
async def TikTok(client: Client, message: Message):
	try:
		link = message.text[3:]
		await message.delete()
		response = requests.get(f"https://api.reiyuura.me/api/dl/tiktok?url={link}").text
		jsons = json.loads(response)
		results = jsons['result']['nowm']
		await client.send_video(message.chat.id,f"{results}")
	except Exception as e:
		await client.send_message(message.chat.id,f"<b>Error:</b> <code>{e}</code>\n\n\n<b>Please send @THE_BURGERNET777</b>")

modules_help.append({"TikTok":[{"tt":"[link to tiktok video]"}]})