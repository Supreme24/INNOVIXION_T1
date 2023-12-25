import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com/news'

# Sending a GET request to the URL
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements with a specific class (you may need to inspect the website to find the appropriate class)
    article_titles = soup.find_all('h2', class_='article-title')

    # Extract and print the titles
    for title in article_titles:
        print(title.text.strip())  # .strip() removes extra whitespaces

else:
    print('Failed to retrieve the webpage.')