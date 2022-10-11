from email import message_from_bytes
import site
from tkinter import NSEW
from bs4 import BeautifulSoup
from requests import get

def news():
  site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
  news = BeautifulSoup(site.text, 'html.parser')
  for item in news.findAll('item')[:2]:
    message = item.title.text

    return message