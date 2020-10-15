import requests
import logging


class DiscordHandler(logging.Handler):
    def __init__(self, username: str,
                 webhook_url: str,
                 avatar_url: str = None):
        logging.Handler.__init__(self)
        self.json_data = {
            "username": username}
        self.webhook_url = webhook_url
        if avatar_url is not None:
            self.json_data["avatar_url"] = avatar_url

    def emit(self, record):
        msg = self.format(record)
        self.json_data["content"] = f"```\n{msg}\n```"
        response = requests.post(self.webhook_url, json=self.json_data)
        response.raise_for_status()
