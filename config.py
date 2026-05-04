import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://sneakerstore.test-api-web.ru/")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "100"))
    TIMEOUT = int(os.getenv("TIMEOUT", "10000"))
    VIDEO = os.getenv("VIDEO", "true").lower() == "true"
    VIDEO_PATH = os.getenv("VIDEO_PATH", "build/testvideo")

config = Config()

