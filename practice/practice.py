import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"
response = requests.get(url)

if response.status_code == 200:
  html_content = response.text
  soup = BeautifulSoup(html_content, 'html.parser')
  title = soup.title.text.strip()
  print('Title:',title)
  
else:
  print ("printo HTML content,page not accessible")
