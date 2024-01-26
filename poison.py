from telethon import events
import asyncio
from ..utils import admin_cmd
from .. import ALIVE_NAME
from .. import CMD_HELP
import importlib.util

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

@borg.on(admin_cmd(pattern="poison"))
from telethon import events
from random import choice as c
from telethon.tl import types
from . import ultroid_bot
@ultroid_bot.on(events.NewMessage(outgoing=True))
async def linkrss(e):

  a = "😍","🔥","❤️","🔥","😊","❤️‍🩹","🥰"
  await e.react([types.ReactionEmoji(f"{c(a)}")],big=True)
