import os
from dotenv import load_dotenv


load_dotenv()

# токен нашего бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# id-list всех админов нашего бота
admins = [
    893018497
]
