#Bobby
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21241424"))
API_HASH = environ.get("API_HASH", "e8318a4df05644acdf6705e1d67280f8")
BOT_TOKEN = environ.get("BOT_TOKEN", "7811042291:AAHQdxQHvnjUPcmVfUmo43mijyzllJv6bVM")
OWNER = int(environ.get("OWNER", "7323329628"))
CREDIT = environ.get("CREDIT", "@KingXHD")
AUTH_USER = os.environ.get('AUTH_USERS', '7323329628').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
