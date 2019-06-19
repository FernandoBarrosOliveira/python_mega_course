import requests
from bs4 import BeautifulSoup

URL_1 = "http://versoes.milenioerp.com.br//builds?page="
QTD_PAGES = 3
list_ml = [
"ML-18197",
"ML-18478",
"ML-18522",
"ML-18491",
"ML-18299",
"ML-18331",
"ML-18393",
"ML-18458",
"ML-18530",
"ML-18580",
"ML-18582",
"ML-18583",
"ML-18586",
"ML-18588",
"ML-18605",
"ML-18606",
"ML-18608",
"ML-18613",
"ML-18650"]

list_all = []

for i in range(QTD_PAGES +1):
  req = requests.get(URL_1 + str(i))
  soap = BeautifulSoup(req.content, "html.parser")
  all = soap.find_all("span", {"class":"secondary label"})  
  list_all.append(all)

#print(''.join(list_all))  
list_free = []
list_trap = []
# for items in list_all:
#   for item in items:    
#     if item.text in list_ml:
#       list_free.append(item.text)
#     else :
#       list_trap.append(item.text)

for item in list_ml:
  if item in list_all:
    list_free.append(item)
  else :
    list_trap.append(item)

print ("ML liberadas :")
print (*list_free, sep= ", ")
print("ML n?o liberadas: ")
print (*list_trap, sep= ", ")

