import requests      #requests:library used to make HTTP requests to websites.to fetch the content of a web page
from bs4 import BeautifulSoup #This library is a Python parser designed to extract data from HTML and XML documents


url = "https://www.youtube.com/"  #This url variable stores the web address (URL) of the website you want to scrape

response = requests.get(url)  #used requests library to send a GET request to the specified URL. 

if response.status_code == 200:#This attribute of the response object contains HTTP status code returned by website.
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.title.text.strip()
    print("Title:", title)
else:
    print("No HTML content, Page not accessible")

