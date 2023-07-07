import requests

from bs4 import BeautifulSoup


def main():
    url = input("Input the URL:\n")
    # get_jason(url)
    get_html(url)

def get_jason(url):
    r = requests.get(url)
    if r:
        print(r.json()['content'])
    else:
        print("Invalid quote resource!")

def get_html(url):
    if url.startswith('https://www.nature.com') and \
        'article' in url:
        info = dict()
        r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find('title')
        info["title"] = title.text
        description = soup.find('meta', {'name': 'description'})
        info["description"] = description.text
        print(info)
    else:
        print('Invalid page!')


if __name__ == '__main__':
    main()
