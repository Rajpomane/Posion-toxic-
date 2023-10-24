"""COMMAND : .poison"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="poison"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "poison":

    await event.edit("🚩🚩")

    animation_chars = [

            "🚩🚩\n  🔥❤️  =====> MULLO TUMHARI MAA KA BHOSDA",
            "🚩🚩\n  🔥❤️  =====> MULLO KI MAA KI CUUTTTTTTTTTT",    
            "🚩🚩\n  🔥❤️  =====> LAND LAND MULLE",
            "🚩🚩\n  🔥❤️  =====> LAND LAND ISLAM ",
            "🚩🚩\n  🔥❤️  =====> MULLO KI MAA KI CHUT ME HCL HAHAA",    
            "🚩🚩\n  🔥❤️  =====> MULLO KI MAA KE BHOSDE ME TV",
            "🚩🚩\n  🔥❤️  =====> MULLO KI BHAN KA BHOSDA HAHA",
            "🚩🚩\n  🔥❤️  =====> BURKHA UTAR KE GAND MAR DUNGA HAHA",    
            "🚩🚩\n  🔥❤️  =====> LAND PE MULLE LAND PE ISLAM ",
            "🚩🚩\n  🔥❤️  =====> MADE BY POISON ❤️💫 JAI SHREE RAM HAR HAR MAHADEV 🚩🔥❤️"
            "🚩🚩\n  🔥❤️  =====> COME BACK BABY 🖤🥂 DANGEROUS ALWAYS OP 🚩🔥❤️"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
