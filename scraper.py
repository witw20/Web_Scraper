import requests, string, os

from bs4 import BeautifulSoup


def main():
    page_num = int(input("page:\n"))
    input_type = input("type of articles:\n")
    for page in range(1, page_num + 1):
        try:
            os.mkdir('Page_' + str(page))
        except FileExistsError:
            os.chdir("./Page_"+ str(page))
        else:
            os.chdir("./Page_"+ str(page))
        url = r"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=" + str(page)
        get_article(url, input_type)
        os.chdir("..")
        print('Saved all articles.')

def get_article(url, input_type):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            article_type = article.find('span', {'class': 'c-meta__type'}).text
            if article_type == input_type:
                link = article.find('a', {'data-track-action': 'view article'}).get('href')
                write_article('https://www.nature.com' + link)
    else:
        print("The page returned", r.status_code, "!")


def write_article(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        title = soup.find('title').text
        file_name = ''.join(["_" if x in string.punctuation or x == " " else x for x in title])
        file = open(file_name + '.txt', 'wb')
        file.write(soup.find('p', {"class": "article__teaser"}).text.encode('utf-8'))
        file.close()
        print("Content saved:", file_name + '.txt')
    else:
        print("The URL returned", r.status_code, "!")


if __name__ == '__main__':
    main()
