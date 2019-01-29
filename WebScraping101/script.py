import requests
from bs4 import BeautifulSoup

URL_1 = "http://versoes.milenioerp.com.br/"

req = requests.get(URL_1)
soap = BeautifulSoup(req.content, "html.parser")
all = soap.find_all("span", {"class":"secondary label"})
for item in all:
  print(item.text)
