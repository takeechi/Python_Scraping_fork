import requests
from bs4 import BeautifulSoup


def main():
    p = requests.get('https://github.com/FujiiNoritsugu')
    soup = BeautifulSoup(p.text)
    for a in soup.find_all('a'):
        print(a.get('href'))


if __name__ == '__main__':
    main()
