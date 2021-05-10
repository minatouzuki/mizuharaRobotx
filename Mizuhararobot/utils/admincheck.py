from pyrogram.types import Message


async def admin_check(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    check_status = await client.get_chat_member(
        chat_id=chat_id,
        user_id=user_id
    )
    admin_strings = [
        "creator",
        "administrator"
    ]
    return check_status.status in admin_strings


async def owner_check(message: Message) -> bool:
    client = message._client
    chat_id = message.chat.id
    user_id = message.from_user.id

    user = await client.get_chat_member(chat_id=chat_id, user_id=user_id)

    if user.status != "creator":
        await message.reply_text(
            "This is an Owner Restricted command and you're not allowed to use it."
        )
        return False

    return True
