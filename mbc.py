import os
import requests
from bs4 import BeautifulSoup

query='연예인'
search_url=f'https://search.imbc.com/news?qt={query}'
response=requests.get(search_url)
soup=BeautifulSoup(response.text, 'html.parser')
print(soup)