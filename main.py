import json
from google.cloud import pubsub_v1 
from google.auth import jwt
import notifier

# Notifier Configuration
channels = []
channels.append(
    notifier.Channel(
        "default",
        [notifier.Notification("gchat","https://chat.googleapis.com/v1/spaces/AAAA5F9mVto/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=EnUegHHKtFNMJ4_pqppfRgwrZnbm7jPt6HASQBOXOEs"),
         notifier.Notification("email", "the.daddy.magoo@gmail.com")]
    )
)

# Subscription Configuration
subscription_name = 'projects/cobalt-catalyst-114520/subscriptions/notifications-sub'
service_account_info = json.load(open("pubsub-key.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(message)
    
    for c in channels:
        if c.name == message.attributes["channel"]:
            for n in c.notifications:
                if n.type == "gchat":
                    notifier.GChat.send(message.data.decode(), n.config)
                elif n.type == "email":
                    notifier.Email.send(message.data.decode(), n.config)

    message.drop()

streaming_pull_future = subscriber.subscribe(subscription_name, callback=callback)
print(f"Listening for messages on {subscription_name}..\n")

with subscriber:
    try:
        streaming_pull_future.result(timeout=5.0)
    except:
        pass