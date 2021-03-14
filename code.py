import requests
from bs4 import BeautifulSoup



base_url='https://www.dailymail.co.uk/home/index.html'
def gettext(base_url):
    req=requests.get(base_url)
    soup=BeautifulSoup(req.content,"html.parser")
    title=soup.title.get_text().strip
    with open(r'C:\Users\Celal\PycharmProjects\crawwllwlw\ptitle.txt','w') as f:
        f.write(title)
def gethtml(base_url):
    req=requests.get(base_url)
    soup=BeautifulSoup(req.content,'html.parser')
    with open(r'C:\Users\Celal\PycharmProjects\crawwllwlw\ptitle.txt', 'w') as f:
        f.write(soup)
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
gettext(base_url)
gethtml(base_url)
