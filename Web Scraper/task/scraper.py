from bs4 import BeautifulSoup
import os
import requests
import string


def get_soup(url):
    response = requests.get(url)
    if response:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f'\nThe URL {url} returned {response.status_code}!')
        exit()


def process_title(text):
    text = ''.join(x for x in text if x not in string.punctuation)
    return text.strip().replace(' ', '_')


def save_to_file(name, content):
    file = open(f'{name}.txt', 'wb')
    file.write(bytes(content, encoding='utf-8'))
    file.close()


def save_articles(data, a_type, url):
    saved = []
    for art in data:
        if art.find('span', {'data-test': 'article.type'}).text.strip() == a_type:
            title = art.find('a').text
            art_link = url + art.find('a', {'data-track-action': 'view article'}).get('href')
            article = get_soup(art_link)
            body = article.find('div', {'class': 'c-article-body'}).text.strip()
            save_to_file(process_title(title), body)
            saved.append(title)
    return saved


def set_dir(p, s_dir):
    page_dir = os.path.join(s_dir, f'Page_{p}')
    if not os.access(page_dir, os.F_OK):
        os.mkdir(page_dir)
    os.chdir(page_dir)


def main():
    end_page = int(input('Pages: '))
    art_type = input('Article type: ')
    url_base = 'https://www.nature.com'
    path = '/nature/articles?sort=PubDate&year=2020'
    save_dir = os.getcwd()
    saved = []
    for page in range(1, end_page + 1):
        soup = get_soup(url_base + path + f'&page={page}')
        articles = soup.find_all('article')
        set_dir(page, save_dir)
        saved.extend(save_articles(articles, art_type, url_base))
    print('Saved articles:\n' + '\n'.join(saved))


if __name__ == '__main__':
    main()
