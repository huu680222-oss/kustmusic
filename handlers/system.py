import os
import time

import psutil
from pyrogram import Client as PyroClient
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import state
from config import API_ID, API_HASH, COOKIES_FILE, MAIN_OWNER
from core.guards import check_abuse
from core.helpers import get_readable_time, to_bold_unicode


async def ping_handler(client, message):
    start = time.time()
    response = await message.reply_text("🏓 **Pinging...**")
    tg_ping = round((time.time() - start) * 1000)

    cookies_status = "Inactive ❌"
    if COOKIES_FILE and os.path.exists(COOKIES_FILE) and os.path.getsize(COOKIES_FILE) > 0:
        cookies_status = "Active ✅"

    uptime = get_readable_time(int(time.time() - state.bot_start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    msg = (
        f"🏓 <b>Pong!</b>\n\n"
        f"📱 <b>Telegram:</b> <code>{tg_ping}ms</code>\n"
        f"🍪 <b>Cookies:</b> <code>{cookies_status}</code>\n\n"
        f"<blockquote>💻 <b>System</b>\n"
        f"├ <b>Uptime:</b> <code>{uptime}</code>\n"
        f"├ <b>CPU:</b> <code>{cpu}%</code>\n"
        f"├ <b>RAM:</b> <code>{mem}%</code>\n"
        f"└ <b>Disk:</b> <code>{disk}%</code></blockquote>"
    )
    await response.edit_text(msg, parse_mode=ParseMode.HTML)


START_IMAGES = [
    "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1000&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=1000&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=1000&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?q=80&w=1000&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=1000&auto=format&fit=crop"
]

async def start_handler(client, message):
    if await check_abuse(message.from_user.id):
        return

    import random
    user_link = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
    bot_name_bold = to_bold_unicode(client.me.first_name.upper())

    caption = (
        f"👋 <b>ʜєʏ</b> {user_link}<b>!</b>\n\n"
        f"<blockquote>🎵 <b>{bot_name_bold}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎧 <b>ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠᴄ ᴍᴜsɪᴄ sᴛʀєᴀᴍɪɴɢ</b>\n"
        f"⚡ <b>ʏᴛ-ᴅʟᴘ ᴘᴏᴡєʀєᴅ — ɪɴsᴛᴀɴᴛ sᴘєєᴅ</b>\n"
        f"🤖 <b>ᴄʟᴏɴє sʏsᴛєᴍ — ʜᴏsᴛ ʏᴏᴜʀ ᴏᴡɴ</b>\n"
        f"🛡️ <b>ʙᴜɪʟᴛ-ɪɴ ɢʀᴏᴜᴘ ᴘʀᴏᴛєᴄᴛɪᴏɴ</b>\n"
        f"🌱 <b>ᴢєʀᴏ ᴅᴀᴛᴀʙᴀsє ɴєєᴅєᴅ</b></blockquote>\n\n"
        f"⚡ <b>ᴘᴏᴡєʀєᴅ ʙʏ:</b> <a href='https://t.me/zolvid'>ᴢᴏʟᴠɪᴅ</a>\n"
        f"💡 <i>ᴜsє /play &lt;sᴏɴɢ&gt; ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴛᴀʀᴛ!</i>"
    )

    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [
            InlineKeyboardButton("📜 ʜєʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="show_help"),
            InlineKeyboardButton("👤 ᴏᴡɴєʀ", url="https://t.me/zolvid"),
        ],
        [
            InlineKeyboardButton("💬 ᴄʜᴀɴɴєʟ", url="https://t.me/zolvid"),
            InlineKeyboardButton("✨ sᴜᴘᴘᴏʀᴛ", url="https://t.me/zolvid"),
        ]
    ]

    photo_url = random.choice(START_IMAGES)
    try:
        await client.send_photo(
            chat_id=message.chat.id,
            photo=photo_url,
            caption=caption,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    except Exception as e:
        await message.reply_text(
            caption,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons)
        )


async def clone_command(client, message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply_text(
            "❌ <b>Usage:</b> <code>/clone BOT_TOKEN</code>\n\n"
            "<blockquote>📖 <b>How to get a bot token:</b>\n"
            "1. Open @BotFather\n"
            "2. Send /newbot and follow steps\n"
            "3. Copy the token and paste it here</blockquote>",
            parse_mode=ParseMode.HTML,
        )

    token = message.command[1]
    status = await message.reply_text("⏳ <b>Initializing clone...</b>", parse_mode=ParseMode.HTML)
    try:
        new_client = PyroClient(
            f"clone_{token.split(':')[0]}", api_id=API_ID, api_hash=API_HASH, bot_token=token
        )
        await new_client.start()
        me = await new_client.get_me()
        new_client.clone_owner = user_id
        new_client.is_main = False

        from handlers.router import register_handlers
        register_handlers(new_client)
        state.active_clients[me.id] = new_client

        clone_count = len([c for c in state.active_clients.values() if not getattr(c, "is_main", False)])

        await status.edit_text(
            f"✅ <b>Bot cloned successfully!</b>\n\n"
            f"<blockquote>🤖 <b>Bot:</b> @{me.username}\n"
            f"👑 <b>Owner:</b> <code>{user_id}</code>\n"
            f"🔢 <b>Total clones:</b> <code>{clone_count}</code></blockquote>",
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        await status.edit_text(f"❌ <b>Clone failed:</b>\n<code>{e}</code>", parse_mode=ParseMode.HTML)


async def active_bots_command(client, message):
    if message.from_user.id != MAIN_OWNER:
        return await message.reply_text("❌ <b>Restricted to main owner.</b>", parse_mode=ParseMode.HTML)

    if not state.active_clients:
        return await message.reply_text("❌ <b>No active bots found.</b>", parse_mode=ParseMode.HTML)

    text = f"🌐 <b>Active Bots</b> — Total: {len(state.active_clients)}\n\n"
    for _, c in state.active_clients.items():
        username = c.me.username if c.me else "Unknown"
        owner = getattr(c, "clone_owner", "Main")
        tag = "✅ Main" if getattr(c, "is_main", False) else f"🔗 Clone · Owner: <code>{owner}</code>"
        text += f"├ @{username} · {tag}\n"

    await message.reply_text(text, parse_mode=ParseMode.HTML)
