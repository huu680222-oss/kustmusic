import asyncio

from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import state
from core.guards import is_admin
from core.playback import play_music_core
from handlers.music import clear_command, pause_command, resume_command, skip_command, stop_command
from handlers.system import start_handler

from core.helpers import to_bold_unicode
from config import MAIN_OWNER

async def edit_msg(query, text, reply_markup):
    if query.message.photo:
        try:
            await query.message.edit_caption(
                caption=text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.HTML
            )
        except Exception:
            pass
    else:
        try:
            await query.message.edit_text(
                text=text,
                reply_markup=reply_markup,
                parse_mode=ParseMode.HTML
            )
        except Exception:
            pass


async def callback_handler(client, query: CallbackQuery):
    data = query.data
    chat_id = query.message.chat.id
    user_id = query.from_user.id

    if data == "progress":
        return await query.answer("🎵 Live Playback")

    if data == "verify_assistant":
        if not await is_admin(client, chat_id, user_id):
            return await query.answer("❌ Admin only!", show_alert=True)
        if chat_id in state.chat_queues and state.chat_queues[chat_id]:
            await query.message.edit_text("🔄 <b>Continuing playback...</b>", parse_mode=ParseMode.HTML)
            asyncio.create_task(play_music_core(client, chat_id, state.chat_queues[chat_id][0], query.message))
        else:
            await query.message.edit_text("❌ <b>Queue is empty.</b>", parse_mode=ParseMode.HTML)
        return

    if data == "show_help":
        buttons = [
            [
                InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="help_music"),
                InlineKeyboardButton("🛡️ ᴀᴅᴍɪɴ", callback_data="help_admin"),
            ],
            [
                InlineKeyboardButton("⚙️ sʏsᴛєᴍ", callback_data="help_system"),
                InlineKeyboardButton("🏠 ʙᴀᴄᴋ", callback_data="go_back"),
            ],
            [
                InlineKeyboardButton("👤 ᴏᴡɴєʀ", url="https://t.me/zolvid")
            ]
        ]
        text = (
            "📜 <b>ʜєʟᴘ & ᴄᴏᴍᴍᴀɴᴅs ᴍєɴᴜ</b>\n\n"
            "<blockquote>ᴄʟɪᴄᴋ ᴏɴ ᴛʜє ʙᴜᴛᴛᴏɴs ʙєʟᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀє ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛᴏ ᴜsє ᴛʜє ᴍᴜsɪᴄ ʙᴏᴛ!</blockquote>\n\n"
            "⚡ <b>ᴘᴏᴡєʀєᴅ ʙʏ:</b> <a href='https://t.me/zolvid'>ᴢᴏʟᴠɪᴅ</a>"
        )
        return await edit_msg(query, text, InlineKeyboardMarkup(buttons))

    if data == "go_back":
        user_link = f"<a href='tg://user?id={query.from_user.id}'>{query.from_user.first_name}</a>"
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
        return await edit_msg(query, caption, InlineKeyboardMarkup(buttons))

    if data == "help_music":
        buttons = [
            [
                InlineKeyboardButton("🛡️ ᴀᴅᴍɪɴ", callback_data="help_admin"),
                InlineKeyboardButton("⚙️ sʏsᴛєᴍ", callback_data="help_system"),
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ʜєʟᴘ", callback_data="show_help"),
                InlineKeyboardButton("🏠 ᴍᴀɪɴ ᴍєɴᴜ", callback_data="go_back"),
            ]
        ]
        text = (
            "<blockquote>🎵 <b>ᴍᴜsɪᴄ ᴄᴏᴍᴍᴀɴᴅs</b></blockquote>\n\n"
            "❍ <code>/play &lt;sᴏɴɢ ɴᴀᴍє/ᴜʀʟ&gt;</code> — ᴘʟᴀʏ sᴏɴɢ ᴏʀ ʏᴏᴜᴛᴜʙє ᴜʀʟ ɪɴ ᴠᴄ\n"
            "❍ <code>/p &lt;sᴏɴɢ ɴᴀᴍє/ᴜʀʟ&gt;</code> — sʜᴏʀᴛᴄᴜᴛ ғᴏʀ /play\n"
            "❍ <code>/vplay &lt;sᴏɴɢ ɴᴀᴍє/ᴜʀʟ&gt;</code> — ᴘʟᴀʏ ᴠɪᴅєᴏ ɪɴ ᴠᴄ (sᴘᴏɪʟєʀ ᴛʜᴜᴍʙɴᴀɪʟ)\n"
            "❍ <code>/vp &lt;sᴏɴɢ ɴᴀᴍє/ᴜʀʟ&gt;</code> — sʜᴏʀᴛᴄᴜᴛ ғᴏʀ /vplay\n"
            "❍ <code>/skip</code> — sᴋɪᴘ ᴄᴜʀʀєɴᴛ sᴏɴɢ\n"
            "❍ <code>/stop</code> — sᴛᴏᴘ ᴘʟᴀʏʙᴀᴄᴋ ᴀɴᴅ ʟєᴀᴠє ᴠᴄ\n"
            "❍ <code>/pause</code> — ᴘᴀᴜsє ᴘʟᴀʏʙᴀᴄᴋ\n"
            "❍ <code>/resume</code> — ʀєsᴜᴍє ᴘʟᴀʏʙᴀᴄᴋ\n"
            "❍ <code>/clear</code> — ᴄʟєᴀʀ ǫᴜєᴜєᴅ sᴏɴɢs\n\n"
            "⚡ <b>ᴘᴏᴡєʀєᴅ ʙʏ:</b> <a href='https://t.me/zolvid'>ᴢᴏʟᴠɪᴅ</a>"
        )
        return await edit_msg(query, text, InlineKeyboardMarkup(buttons))

    if data == "help_admin":
        buttons = [
            [
                InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="help_music"),
                InlineKeyboardButton("⚙️ sʏsᴛєᴍ", callback_data="help_system"),
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ʜєʟᴘ", callback_data="show_help"),
                InlineKeyboardButton("🏠 ᴍᴀɪɴ ᴍєɴᴜ", callback_data="go_back"),
            ]
        ]
        text = (
            "<blockquote>🛡️ <b>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs</b></blockquote>\n\n"
            "❍ <code>/kick</code> — ᴋɪᴄᴋ ᴀ ᴍєᴍʙєʀ (ʀєᴘʟʏ)\n"
            "❍ <code>/ban</code> — ʙᴀɴ ᴀ ᴍєᴍʙєʀ (ʀєᴘʟʏ)\n"
            "❍ <code>/unban</code> — ᴜɴʙᴀɴ ᴀ ᴍєᴍʙєʀ (ʀєᴘʟʏ)\n"
            "❍ <code>/mute</code> — ᴍᴜᴛє ᴀ ᴍєᴍʙєʀ (ʀєᴘʟʏ)\n"
            "❍ <code>/unmute</code> — ᴜɴᴍᴜᴛє ᴀ ᴍєᴍʙєʀ (ʀєᴘʟʏ)\n\n"
            "⚡ <b>ᴘᴏᴡєʀєᴅ ʙʏ:</b> <a href='https://t.me/zolvid'>ᴢᴏʟᴠɪᴅ</a>"
        )
        return await edit_msg(query, text, InlineKeyboardMarkup(buttons))

    if data == "help_system":
        buttons = [
            [
                InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="help_music"),
                InlineKeyboardButton("🛡️ ᴀᴅᴍɪɴ", callback_data="help_admin"),
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ ᴛᴏ ʜєʟᴘ", callback_data="show_help"),
                InlineKeyboardButton("🏠 ᴍᴀɪɴ ᴍєɴᴜ", callback_data="go_back"),
            ]
        ]
        text = (
            "<blockquote>⚙️ <b>sʏsᴛєᴍ & ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs</b></blockquote>\n\n"
            "❍ <code>/ping</code> — ᴄʜєᴄᴋ ʙᴏᴛ's ᴘɪɴɢ ᴀɴᴅ sᴛᴀᴛs\n"
            "❍ <code>/clone &lt;ʙᴏᴛ_ᴛᴏᴋєɴ&gt;</code> — ᴄʟᴏɴє ᴀ ɴєᴡ ɪɴsᴛᴀɴᴄє ᴏғ ʙᴏᴛ\n"
            "❍ <code>/active</code> — ʟɪsᴛ ᴀʟʟ ᴀᴄᴛɪᴠє ᴄʟᴏɴєs (ᴏᴡɴєʀ ᴏɴʟʏ)\n\n"
            "⚡ <b>ᴘᴏᴡєʀєᴅ ʙʏ:</b> <a href='https://t.me/zolvid'>ᴢᴏʟᴠɪᴅ</a>"
        )
        return await edit_msg(query, text, InlineKeyboardMarkup(buttons))

    if data in ["stop", "skip", "pause", "resume", "clear"]:
        if not await is_admin(client, chat_id, user_id):
            return await query.answer("❌ Admin only!", show_alert=True)
        if data == "stop":
            await stop_command(client, query.message)
        elif data == "skip":
            await skip_command(client, query.message)
        elif data == "pause":
            await pause_command(client, query.message)
        elif data == "resume":
            await resume_command(client, query.message)
        elif data == "clear":
            if chat_id in state.chat_queues and len(state.chat_queues[chat_id]) > 1:
                state.chat_queues[chat_id] = [state.chat_queues[chat_id][0]]
                await query.answer("🗑 Queue cleared.")
                await query.message.edit_text("🗑 <b>Queue cleared.</b>", parse_mode=ParseMode.HTML)
            else:
                await query.answer("❌ Queue is already empty.")
        try:
            await query.answer()
        except Exception:
            pass
