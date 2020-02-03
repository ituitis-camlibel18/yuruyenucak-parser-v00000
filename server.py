import os


from bottle import Bottle, request, template, route
from pathlib import Path
from socket import gethostname, gethostbyname 


import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path

#home
quote_page = 'https://www.sportinglife.com/football/live/86595/teams/home'
#away





"""quote_pageaway = 'https://www.sportinglife.com/football/live/89612/teams/home'
pageaway = urlopen(quote_page)
soup = BeautifulSoup(pageaway, 'html.parser')
numberaway = soup.findAll('div',attrs={'class':'footballPlayerNumber'})
t = numberaway[11]
numberaway.append(t)"""


  
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
number = soup.findAll('div',attrs={'class':'footballPlayerNumber'})
a = number[11]
number.append(a)





"""for temp in number:
  print(temp.getText())"""

"""for tempaway in numberaway:
  print(tempaway.getText())"""
html_list = []
for i in number:
  a = i.getText()
  html_list.append('<li>'+ a + '</li>')
html_list[11] = '<li>-</li>'

        

def numbers1():
  
  

  one = Path("mainpage.html").read_text()
  two = ''
  for x in html_list:
    two +=f'{x}'
  html = one.format(two)
  return html
   
   



def create_app():
    app = Bottle()
    app.route("/", "GET", numbers1)
    app.route("/mainpage.html", "GET", numbers1)
    
    return app

    


application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

    

