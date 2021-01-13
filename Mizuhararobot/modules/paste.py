import asyncio
import aiohttp
import os


async def paste(client, message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    if message.reply_to_message.document and message.reply_to_message.document.file_size < 2 ** 20 * 10:
        var = os.path.splitext(message.reply_to_message.document.file_name)[1]
        print(var)
        path = await message.reply_to_message.download("nana/")
        with open(path, 'r') as doc:
            text = doc.read()
        os.remove(path)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    'https://nekobin.com/api/documents',
                    json={"content": text},
                    timeout=3
            ) as response:
                key = (await response.json())["result"]["key"]
    except Exception:
        await message.edit_text("`Pasting failed`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f'https://nekobin.com/{key}'
        raw_url = f'https://nekobin.com/raw/{key}'
        reply_text = '**Nekofied:**\n'
        reply_text += f' - **Link**: {url}\n'
        reply_text += f' - **Raw**: {raw_url}'
        delete = bool(len(message.command) > 1 and \
                        message.command[1] in ['d', 'del'] and \
                        message.reply_to_message.from_user.is_self)
        if delete:
            await asyncio.gather(
                client.send_message(message.chat.id,
                                    reply_text,
                                    disable_web_page_preview=True
                                    ),
                message.reply_to_message.delete(),
                message.delete()
            )
        else:
            await message.reply(
                reply_text,
                disable_web_page_preview=True,
            )
