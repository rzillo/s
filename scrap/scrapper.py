from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

#maybe other links
link = 'https://www.amazon.com.br/MSI-Gaming-RTX-3080-Trio/dp/B095VZ6F73'
r = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
open_file = urlopen(r)
