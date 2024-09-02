import requests
import os

class GChat:
    def send(text: str, url: str):
        json_data = {
            'text': text
        }
        response = requests.post(url, json=json_data)
        return response
    
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
  