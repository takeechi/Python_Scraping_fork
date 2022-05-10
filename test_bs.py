from bs4 import BeautifulSoup


def main():
    with open('./test_html.html', 'r') as f:
        soup = BeautifulSoup(f.read())
        print(soup.title)

if __name__ == '__main__':
    main()
