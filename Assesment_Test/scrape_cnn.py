import requests
from bs4 import BeautifulSoup   
import csv

 
url = 'https://edition.cnn.com/'
response = requests.get(url)

if response.status_code == 200:
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')

    
    articles = soup.find_all('a', class_='container__title-url container_lead-package__title-url')   

    
    for article in articles:
        title = article.get_text()
        url = article['href']
        full_url = f"https://edition.cnn.com{url}"
        print(f"Title: {title}, URL: {full_url}")

     # Save results to CSV
    with open('cnn_articles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'URL'])   

        for article in articles:
            title = article.get_text()
            url = article['href']
            full_url = f"https://edition.cnn.com{url}"
            writer.writerow([title, full_url])
else:
    print(f"Failed to retrieve page, status code: {response.status_code}")
