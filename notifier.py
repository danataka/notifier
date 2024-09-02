import requests
import mailtrap as mt
import os

class GChat:
    def send(text: str, url: str):
        json_data = {
            'text': text
        }
        response = requests.post(url, json=json_data)
        return response

class Email:
  def send(body:str, toaddress:str):
    mail = mt.Mail(
      sender=mt.Address(email="mailtrap@demomailtrap.com", name="notif.ier"),
      to=[mt.Address(email=f"{toaddress}")],
      subject="Message from notifier",\
      text=f"{body}"
    )
    token = os.environ.get("mt_token")
    client = mt.MailtrapClient(token=f"{token}")
    response = client.send(mail)
    print(response)
    
class Notification:
  def __init__(self, type, config):
    self.type = type
    self.config = config
  def __str__(self):
    return f"{self.type} - {self.config}"

class Channel:
  def __init__(self, name, notifications):
    self.name = name
    self.notifications = notifications
  def __str__(self):
    return f"{self.notifications})"
  def find(self, name: str):
    for n in self.notifications:
      if n.name == name:
        return n
  