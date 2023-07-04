import requests


def main():
    url = input("Input the URL:\n")
    r = requests.get(url)
    if r:
        print(r.json()['content'])
    else:
        print("Invalid quote resource!")

if __name__ == '__main__':
    main()
