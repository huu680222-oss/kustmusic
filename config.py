import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")
elif os.path.exists("kust.env"):
    load_dotenv("kust.env")

def _get_env_int(key: str, default: int) -> int:
    val = os.getenv(key)
    if val is None or val.strip() == "":
        return default
    try:
        return int(val.strip())
    except ValueError:
        return default

API_ID = _get_env_int("API_ID", 29568441)
API_HASH = os.getenv("API_HASH", "b32ec0fb66d22da6f77d355fbace4f2a")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("ASSISTANT_SESSION")
MAIN_OWNER = _get_env_int("OWNER_ID", 8673494392)
DEPLOYED_OWNER_ID = _get_env_int("OWNER_ID", 8673494392)
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")
YOUTUBE_COOKIES = os.getenv("YOUTUBE_COOKIES", "")
RATE_LIMIT_COUNT = 4
RATE_LIMIT_WINDOW = 6
MAX_TITLE_LEN = 30
PORT = _get_env_int("PORT", 8080)
