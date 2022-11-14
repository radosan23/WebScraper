import requests
from bs4 import BeautifulSoup


def main():
    url = input('Input the URL:\n')
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response and 'title' in response.url and 'imdb' in response.url:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text
        description = soup.find('span', {'data-testid': 'plot-l'}).text
        movie = {'title': title, 'description': description}
        print(movie)
    else:
        print('\nInvalid movie page!')


if __name__ == '__main__':
    main()
