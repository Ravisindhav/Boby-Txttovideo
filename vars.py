#Bobby
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27660379"))
API_HASH = environ.get("API_HASH", "19c71c27733f0954371085198855125a")
BOT_TOKEN = environ.get("BOT_TOKEN", "8341331178:AAH9sR16lEOAQqZrDs8Lz8EnhYnbpruBBSs")
OWNER = int(environ.get("OWNER", "5459854363"))
CREDIT = environ.get("CREDIT", "@KingXHD")
AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

