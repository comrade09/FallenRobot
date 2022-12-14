class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = "6435225"
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

    CASH_API_KEY = "NV34OEUX0YAFLUB6" # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://altxcmqe:bqNFRK-cFk3fnTGl4trJHNIxgpRX6SxA@heffalump.db.elephantsql.com/altxcmqe"  # A sql database url from elephantsql.com

    EVENT_LOGS = ("-1001878165791")  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://atharva2:atharva2005@cluster0.m8hdz8r.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "tpxsupport404"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5959631394:AAGZAnzjaDJt0xWnwei-9rXRIuLQL5PHhwg"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "RTHI3DLW56HY"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "1442684727"  # User id of your telegram account (Must be integer)
     

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = ["rss"]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
