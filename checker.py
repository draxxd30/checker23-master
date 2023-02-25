import logging

from pyrogram import Client, filters
from configs import config
from asyncio import sleep
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
    )
import requests
import time
Bot = Client(
        "checker",
        api_hash=config.API_HASH,
        api_id=config.API_ID,
        bot_token=config.BOT_TOKEN,
        plugins=dict(root="plugins"),
        parse_mode="html"
        )

logging.basicConfig(level=logging.INFO)

Bot.run()         