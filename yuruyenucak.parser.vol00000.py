import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pathlib import Path
import os


from bottle import Bottle, request, template, route
from pathlib import Path

#home
quote_page = 'https://www.sportinglife.com/football/live/81718/teams/away'
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
     
html = '<html><body><ul>'
for x in html_list:
  x = f'{x}'
  html = html + x + '</ul></body></html>'
file = open('numbers1.html','w')
file.write(html)
file.close()
