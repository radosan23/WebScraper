import string
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)  # headers={'Accept-Language': 'en-US,en;q=0.5'}
    if response:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f'\nThe URL {url} returned {response.status_code}!')
        exit()


def process_title(text):
    text = ''.join(x for x in text if x not in string.punctuation)
    return text.strip().replace(' ', '_')


def save_to_file(title, content):
    file = open(f'{title}.txt', 'w', encoding='utf-8')
    file.write(content)
    file.close()


def main():
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
    home = 'https://www.nature.com'
    saved = []
    soup = get_soup(url)
    articles = soup.find_all('article')
    for art in articles:
        if art.find('span', {'data-test': 'article.type'}).text.strip() == 'News':
            title = art.find('a').text
            art_link = home + art.find('a', {'data-track-action': 'view article'}).get('href')
            article = get_soup(art_link)
            body = article.find('div', {'class': 'c-article-body'}).text.strip()
            save_to_file(process_title(title), body)
            saved.append(title)
    print('Saved articles:\n' +  '\n'.join(saved))


if __name__ == '__main__':
    main()
