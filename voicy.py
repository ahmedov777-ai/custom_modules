from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions
from ..utils.utils import modules_help, prefix
import asyncio


@Client.on_message(filters.command(["vo", "voicy"], prefix) & filters.me)
async def voice_text(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit("<b>Нету реплай!</b>")
        else:
            if message.reply_to_message.voice:
                await message.edit("<b>Подождите....</b>")
                await client.send_message("@voicybot", "/start")
                await asyncio.sleep(1)
                await message.reply_to_message.forward("@voicybot")
                await asyncio.sleep(3)
                messages = await client.get_history("@voicybot")
                await message.edit(
                    f'<b>Текст:</b>\n{messages[0].text.replace("При поддержке Бородач Инвест"," ")}'
                )
                await client.send(
                    functions.messages.DeleteHistory(
                        peer=await client.resolve_peer(259276793),
                        max_id=0,
                        just_clear=True,
                    )
                )
            else:
                await message.edit("<b>Это не войс!</b>")
    except Exception as e:
        await message.edit(f"<b>Упсс:</b> <code>{e}</code")


modules_help.append(
    {"voicy": [{"voicy": "Сделай реплай на войс и получишь текст из войса)"}]}
)
