import requests
from bs4 import BeautifulSoup


def get_movie(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find('h1').text
    description = soup.find('span', {'data-testid': 'plot-l'}).text
    return {'title': title, 'description': description}


def main():
    url = input('Input the URL:\n')
    response = requests.get(url)  # headers={'Accept-Language': 'en-US,en;q=0.5'}
    if response:
        file = open('source.html', 'wb')
        file.write(response.content)
        file.close()
        print('\nContent saved.')
    else:
        print(f'\nThe URL returned {response.status_code}!')


if __name__ == '__main__':
    main()
