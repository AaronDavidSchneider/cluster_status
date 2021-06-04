from .handler import Handler
from .MITgcm import MITgcmHandler
from .config import ClusterStatusArgparser, read_config, CONF_API_ID, CONF_API_HASH, CONF_BOT_TOKEN, setup
from telethon import TelegramClient


def main(handler):
    conf = read_config()
    with TelegramClient("telegram_simulation_bot", int(conf[CONF_API_ID]), str(conf[CONF_API_HASH])).start(bot_token=str(conf[CONF_BOT_TOKEN])) as telegram_bot:
        handler(telegram_bot)
        print("started telegram_simulation_bot")
        telegram_bot.run_until_disconnected()