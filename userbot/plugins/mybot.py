# Hey There 

from userbot.kimo import *

@icssbot.on(
    icss_cmd(
       pattern="بوتي", outgoing=True
    )
)
async def mybot(k):
    await eor(k, f"**⌔∮ البوت المستخدم - {ICSB}**")
