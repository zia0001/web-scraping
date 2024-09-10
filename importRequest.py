import requests

url = "https://www.facebook.com/"
Response = requests.get(url)
if Response.status_code == 200:
  html_content = Response.text
else:
  print("No HTML content, Page not accesseble")


