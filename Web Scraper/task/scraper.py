import requests


def main():
    url = input('Input the URL:\n')
    response = requests.get(url)
    if response and 'content' in response.json():
        print(response.json()['content'])
    else:
        print('\nInvalid quote resource!')


if __name__ == '__main__':
    main()
