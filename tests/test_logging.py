import logging

from discordlogger.discordhandler import DiscordHandler

def test_logging():
    logger = logging.getLogger("Logging Test")
    webhook_url = input("Discord webhook url: \n")
    dh = DiscordHandler(logger.name, webhook_url)
    formatter = logging.Formatter(
        "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s",
        "%Y-%m-%d %H:%M:%S")
    dh.setFormatter(formatter)
    logger.addHandler(dh)
    logger.error("This is a test log to discord")