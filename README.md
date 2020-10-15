# discordlogger
A handler for the python logging module that sends logs to a discord webhook using a user-defined name and avatar picture.

### Sample Usage

```python
from discordlogger import DiscordHandler
logger = logging.getLogger("SampleLogger")
dh = DiscordHandler(username, webhook_url, avatar_url)
logger.addHandler(dh)
```

`username` is the username the log gets posted from on Discord.
`webhook_url` is the full Discord webhook url.
`avatar_url` is optional and specifies a url to the avatar picture of the Discord webhook.