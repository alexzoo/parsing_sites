import requests
from bs4 import BeautifulSoup as BS


def get_html(url):
    r = requests.get(url=url)
    return r.text


def get_data(html):
    soup = BS(html, 'lxml')
    h1 = soup.select_one('#intro > div.wp-block-columns.is-layout-flex.wp-container-11 > div:nth-child(1) > h1').text
    return h1

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()

