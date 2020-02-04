import os

from bottle import Bottle, request, template, route, redirect
from pathlib import Path
from socket import gethostname, gethostbyname 

import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path

quote_page = 'https://www.sportinglife.com/football/live/86595/teams/away'

def parse():
  global quote_page

  page = urlopen(quote_page)
  soup = BeautifulSoup(page, 'html.parser')
  number = soup.findAll('div',attrs={'class':'footballPlayerNumber'})
  a = number[11]
  number.append(a)

  html_list = []
  for i in number:
    a = i.getText()
    html_list.append('<li>'+ a + '</li>')
  html_list[11] = '<li>-</li>'

  return html_list
    

def numbers1():
  html_list = parse()

  one = Path("mainpage.html").read_text()
  two = ''
  for x in html_list:
    two += f'{x}'
  html = one.format(two)

  return html
   

def linked():
  global quote_page

  link = request.forms.get('link')
  quote_page = link

  redirect("/mainpage.html")


def create_app():
    app = Bottle()
    app.route("/", "GET", numbers1)
    app.route("/mainpage.html", "GET", numbers1)
    app.route("/submitt.html")
    app.route("/linked", "POST", linked)
    
    return app

application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
#1
