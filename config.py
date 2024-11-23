# https://t.me/ultroid_official



import os
import logging
from logging.handlers import RotatingFileHandler

MAX_TOKEN_USES_PER_DAY = int(os.environ.get("MAX_TOKEN_USES_PER_DAY", 1)) # Maximum times a user can use the token in 24 hours   
CREDIT_INCREMENT = int(os.environ.get("CREDIT_INCREMENT", 1)) # The number of credits to increase per token usage
LIMIT_INCREASE_AMOUNT = int(os.environ.get("LIMIT_INCREASE_AMOUNT", 1))# Amount by which the limit is increased after verification


PREMIUM_CREDITS = {
    "Bronze": int(os.environ.get("BRONZE_CREDITS", 50)),  # Default is 50
    "Silver": int(os.environ.get("SILVER_CREDITS", 100)),  # Default is 100
    "Gold": int(os.environ.get("GOLD_CREDITS", 150)),  # Default is 200
}


AUTO_DELETE_DELAY = int(os.environ.get("AUTO_DELETE_DELAY", 1800))# Auti delete time
START_COMMAND_LIMIT = int(os.environ.get("START_COMMAND_LIMIT", 15))# Default limit for new users

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7548080330:AAHRzKtxq0gpj6vER-bPrBs7HonlH0lfOQM")
APP_ID = int(os.environ.get("APP_ID", "22505271"))
API_HASH = os.environ.get("API_HASH", "c89a94fcfda4bc06524d0903977fc81e")
 
BAN = int(os.environ.get("BAN", "1110013191")) #Owner user id
OWNER = os.environ.get("OWNER", "odacchi") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1110013191")) #Owner user id
OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'odacchi')  #Owner username

SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "Alcyone_Support") # WITHOUR @
CHANNEL = os.environ.get("CHANNEL", "AlcyoneBots") # WITHOUR @

AUTO_DELETE = os.environ.get("AUTO_DELETE", True) 

PAYMENT_QR = os.getenv('PAYMENT_QR', 'https://i.ibb.co/BCGJBvd/file-2330.jpg')

PAYMENT_TEXT = os.getenv('PAYMENT_TEXT', """
🎁 <b>Available Subscription Plans:</b>

1. 30 Credit - Bronze Premium - 20₹
2. 50 Credit - Silver Premium - 35₹
3. 50+50 Credit - Gold   Premium - 50₹

To subscribe, click the "Pay via UPI" button below. 
""")



DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://denji3494:denji3494@cluster0.bskf1po.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser10")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002309030392")) #database save channel id 
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001974662693"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))

#Shortner (token system) 
TOKEN = os.environ.get("TOKEN", "verify_") 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "adrinolinks.in") 
SHORTLINK_API = os.environ.get("SHORTLINK_API", "89eebc6996b78477dabf7aebb318fc0e8055e8dc")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 21600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/tutorita/11")

# ignore this one
SECONDS = int(os.getenv("SECONDS", "200")) # auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")
ADMIN_IDS = [6698364560]

try:
    ADMINS=[6698364560]
    for x in (os.environ.get("ADMINS", "6698364560").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join Our Channels To Use Me.\n\nKindly Join Our Channels</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) # remove None and fo this ->: "here come your txt" also with this " " 

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(1110013191)

LOG_FILE_NAME = "uxblogs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

















# https://t.me/ultroid_official
