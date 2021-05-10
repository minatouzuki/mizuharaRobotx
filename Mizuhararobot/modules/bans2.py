import asyncio
import time
from emoji import get_emoji_regexp

from pyrogram import filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.errors import (UsernameInvalid,
                            ChatAdminRequired,
                            PeerIdInvalid,
                            UserIdInvalid)

from Mizuhararobot import (
    DEV_USERS,
    LOGGER,
    OWNER_ID,
    DRAGONS,
    DEMONS,
    TIGERS,
    WOLVES,
)
from Mizuhararobot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_restrict,
    connection_status,
    is_user_admin,
    is_user_ban_protected,
    is_user_in_chat,
    user_admin,
    user_can_ban,
)
from Mizuhararobot.utils.admincheck import admin_check
from Mizuhararobot import pbot


@pbot.on_message(filters.command('ban'))
async def ban_usr(client, message):
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        can_ban = await admin_check(message)

    if is_user_ban_protected(chat, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text("Trying to put me against a God level disaster huh?")
            return log_message
        elif user_id in DEV_USERS:
            message.reply_text("I can't act against our own.")
            return log_message
        elif user_id in DRAGONS:
            message.reply_text(
                "Fighting this Dragon here will put my and peoples life in danger."
            )
            return log_message
        elif user_id in DEMONS:
            message.reply_text(
                "Bring an order from rent association to fight a Demon disaster."
            )
            return log_message
        elif user_id in TIGERS:
            message.reply_text(
                "Bring an order from rent association to fight a Tiger disaster."
            )
            return log_message
        elif user_id in WOLVES:
            message.reply_text("Wolf abilities make them ban immune!")
            return log_message
        else:
            message.reply_text("This user has immunity and cannot be banned.")
            return log_message


        if can_ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.reply("It's not a user!")
                return
            if user_id:
                try:
                    get_mem = await client.get_chat_member(chat_id, user_id)
                    await client.kick_chat_member(chat_id, user_id)
                    await message.reply(
                        f"[{get_mem.user.first_name}](tg://user?id={get_mem.user.id}) **Banned**\n")

                except UsernameInvalid:
                    await message.reply("`invalid username`")
                    return

                except PeerIdInvalid:
                    await message.reply("`invalid username or userid`")
                    return

                except UserIdInvalid:
                    await message.reply("`invalid userid`")
                    return

                except ChatAdminRequired:
                    await message.reply("`You don't have rights to ban members here`")
                    return

                except Exception as e:
                    await message.reply(f"**Log:** `{e}`")
                    return

        else:
            await message.reply("`You don't have enough rights`")
            return
    else:
        await message.delete()
