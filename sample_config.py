#----------------------------------- https://github.com/m4mallu/gofilesbot --------------------------------------------#

import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "gofilesbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5830668557:AAGKCYcd5RAmPEJqXNQ9D0KoRUU4OlJ4TqA")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9100170"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "8bd74422e5a71ca6a5b00bcbdb1bfa48")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQCs5pTl7Kjxud0MAgBJ44iU5wg2LJIInQ0tIyBG_T77cm7XghZ7HdY3-l0MqVpdR170SVTSgE87mFKcY9K5E8t4NzejcsD4VA81Fe61QqGgG-M60XnCxkjRj0tPs6CmJUcpobv4IJn3dDwkCDTX77QN5w5lzzOQHTW0c8piNhpHh9j_VGXUhpPqgrQu1jJFhkHcRAZJb7i9mqhURhIoowmGE3CSvxjdZo7TVJeGcO5UMYxf55TfMgtdMEzB_Hmu4j2kYCeYWEjjq04YdnhrYkYwIb9jFACXBDSGgMpCo49g1W7H_mwBiUCmM4cHguChWfIvN7hmCX5aq7kiSHEfxPCVRclWggA")

    # ID of Channels from which the bot should search files
    CHANNELS = set(int(x) for x in os.environ.get("CHANNELS", "-1001475622139").split())

    # Authorized users to perform delete messages in group
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1170822786").split())

# ------------------------------------------ Optional Variables ------------------------------------------------------ #
    # Username of the group to tag in sending medias
    GROUP = os.environ.get("GROUP", "-1001405795406")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
