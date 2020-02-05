# Installing
```
pip install slack_bundle
```

# Configuring
In config/config.yml just provide the slack token
```
slack:
   token: asdfjklasdhjkj
```

# Using
Just inject the SlackClient and use it!

```
from slackclient import SlackClient
import inject

sc = inject.instance(SlackClient)
channel = "my-slack-channel"
body = "Hey all, I'm a bot!"
sc.api_call(
    method="chat.postMessage",
    channel=channel,
    text=body
)

```


