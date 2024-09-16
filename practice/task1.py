import requests
from bs4 import BeautifulSoup

# CNN homepage URL
url = 'https://edition.cnn.com/'

# Fetch the HTML content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article titles and their corresponding URLs
    # CNN might use <h3> with class 'cd__headline', or sometimes just <a> tags within <h2> or <h3>
    articles = soup.find_all('h3', class_='cd__headline')

    # Loop through each article and extract title and URL
    for article in articles:
        title_tag = article.find('a')
        if title_tag:
            title = title_tag.get_text().strip()
            link = title_tag['href']

            # Handle relative URLs by adding the base URL
            if not link.startswith('http'):
                link = 'https://edition.cnn.com' + link

            # Print the title and URL
            print(f"Title: {title}")
            print(f"URL: {link}")
            print('---')

    # If no articles were found in <h3>, try looking for other common tags
    if not articles:
        print("No articles found in <h3>. Checking <a> tags...")

        # Sometimes articles may be directly in <a> tags (as fall-back)
        fallback_articles = soup.find_all('a')

        for article in fallback_articles:
            if article.get_text().strip():  # Ensure the tag has text content
                title = article.get_text().strip()
                link = article['href']

                # Handle relative URLs
                if not link.startswith('http'):
                    link = 'https://edition.cnn.com' + link

                # Print the title and URL
                print(f"Title: {title}")
                print(f"URL: {link}")
                print('---')

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
