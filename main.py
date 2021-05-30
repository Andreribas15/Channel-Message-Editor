import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
        "Channel Message Editor Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

@FayasNoushad.on_message(filters.private & filters.reply & ((filters.media | filters.text) & ~filters.forward & ~filters.edit))
async def post(bot, update):
    if "-100" not in update.text:
        return
    try:
        user = await bot.get_chat_member(update.text, update.chat.id)
        if (user.status != "administrator") and (user.can_post_messages != True):
            await update.reply_text("You can't do that")
            return
    except Exception:
        return
    try:
        post = await bot.copy_message(
            chat_id=update.text
            from_chat_id=update.reply_to_message.chat.id,
            message_id=update.reply_to_message.message_id,
            reply_markup=update.reply_to_message.reply_markup
        )
        post_link = "https://telegram.me/" + str(post.chat.id) + "/" + str(post.message_id)
        await update.reply_text(
            text="Posted Successfully",
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton(text="Post", url=post_link)
                ]]
            )
        )
    except Exception:
        pass

@FayasNoushad.on_message(filters.private & filters.reply & filters.commands(["edit"]))
async def edit(bot, update):
    if update.text == "/edit":
        return
    if " " in update.text:
        command, link = update.text.split(" ", 1)
    else:
        return
    if "/" in link:
        domain, channel, message_id = update.text.split("/", -2)
    else:
        return
    try:
        user = await bot.get_chat_member(update.text, update.chat.id)
        if (user.status != "administrator") and (user.can_post_messages != True):
            await update.reply_text("You can't do that")
            return
    except Exception:
        return
    if update.reply_to_message.text:
        await bot.edit_message_text(
            chat_id=channel,
            message_id=message_id,
            text=reply_to_message.text,
            reply_markup=reply_to_message.reply_markup,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text("I can edit text only")

FayasNoushad.run()