import json

from Component.Logger import Logger

logger = Logger(1)

with open("config.json", "r") as f:
    config = json.load(f)