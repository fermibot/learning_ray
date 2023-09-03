import ray

urls = ray.data.from_items(["https://www.google.com/"])


def fetch_page(url):
    import requests
    return requests.get(url=url).json()


pages = urls.map(fetch_page)

if __name__ == '__main__':
    print(pages.take(0))
