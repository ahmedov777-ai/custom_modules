from pyrogram import Client, filters
from pyrogram.types import Message
from ..utils.utils import modules_help, prefix
from random import randint
from os import system, remove

try:
    from wget import download
except:
    system("pip install wget")
    system("python main.py")


def download_sticker(url):
    download(url, "f.webp")


@Client.on_message(filters.command(["f"], prefix) & filters.me)
async def random_stiker(client, message):
    await message.delete()
    random = randint(1, 63)
    if random < 10:
        index = f"00{random}"
    else:
        index = f"0{random}"

    sticker = (
        f"https://www.chpic.su/_data/stickers/f/FforRespect/FforRespect_{index}.webp"
    )
    download_sticker(sticker)
    await client.send_sticker(chat_id=message.chat.id, sticker="f.webp")
    remove("f.webp")


modules_help.append({"f": [{"f": "Send f to pay respect"}]})
