# Credit @FeriEXP

import asyncio
import html
import os
import re
import sys
import aiohttp

from aiohttp import ClientSession
from wbb import SUDOERS, TOKEN, app
from pyrogram import Client, filters
from pyrogram.types import Message


__MODULE__ = "anu"

__HELP__ = """/banall- siapa Yang Mau Lu Ancurin!!"""

@app.on_message(filters.command("banall") & filters.group & SUDOERS)

async def ban_all(c: Client, m: Message):

    chat = m.chat.id

    async for member in c.get_chat_members(chat):

        user_id = member.user.id

        url = (f"https://api.telegram.org/bot{TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")

        async with aiohttp.ClientSession() as session:

            await session.get(url)
