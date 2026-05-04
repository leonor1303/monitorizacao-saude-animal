import requests
from bs4 import BeautifulSoup

urls = [
    "https://pt.wikipedia.org/wiki/Leishmaniose",
    "https://pt.wikipedia.org/wiki/Parvovirose"
]

with open("outputs/doencas.txt", "w", encoding="utf-8") as f:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        titulo = soup.find("h1").text
        paragrafo = soup.find("p").text

        print(titulo)
        print(paragrafo)

        f.write(titulo + "\n")
        f.write(paragrafo + "\n\n")
      
