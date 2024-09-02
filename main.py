import json
from google.cloud import pubsub_v1 
from google.auth import jwt

service_account_info = json.load(open("key.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id='cobalt-catalyst-114520',
    sub='notifications-sub'
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)


def callback(message):
    print(message)
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_name, callback=callback)
print(f"Checking for messages on {subscription_name}..\n")

with subscriber:
    try:
        streaming_pull_future.result(timeout=2.0)
    except:
        pass