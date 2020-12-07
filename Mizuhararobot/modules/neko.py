import requests
import nekos
from PIL import Image
import os

from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async

from Mizuhararobot import dispatcher, updater


def is_user_in_chat(chat: Chat, user_id: int) -> bool:
    member = chat.get_member(user_id)
    return member.status not in ("left", "kicked")


@run_async
def neko(bot: Bot, update: Update):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))




@run_async
def poke(bot: Bot, update: Update):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))



@run_async
def waifu(bot: Bot, update: Update):
    msg = update.effective_message
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")






@run_async
def hug(bot: Bot, update: Update):
    msg = update.effective_message
    target = "cuddle"
    msg.reply_video(nekos.img(target))





@run_async
def foxgirl(bot: Bot, update: Update):
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))



@run_async
def baka(bot: Bot, update: Update):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))


@run_async
def tickle(bot: Bot, update: Update):
     msg = update.effective_message
     target = "tickle"
     msg.reply_video(nekos.img(target))

@run_async
def feed(bot: Bot, update: Update):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

@run_async
def smug(bot: Bot, update: Update):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))




NEKO_HANDLER = CommandHandler("neko", neko)
WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper)
TICKLE_HANDLER = CommandHandler("tickle", tickle)
FEED_HANDLER = CommandHandler("feed", feed)
POKE_HANDLER = CommandHandler("poke", poke)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl)
SMUG_HANDLER = CommandHandler("smug", smug)
BAKA_HANDLER = CommandHandler("baka", baka)
CUDDLE_HANDLER = CommandHandler("hug", hug)


dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
