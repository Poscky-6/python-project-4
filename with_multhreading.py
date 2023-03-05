"""
We either want to created multiple processes

** OR **

We want to create multiple threads to achieve the same task


"""

import requests
import time

from multiprocessing.pool import ThreadPool


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[ INFO ] total time to execute :: {end}")
        return result

    return wrapper


"""

thread-1  https://swapi.dev/api/people/1
thread-2  https://swapi.dev/api/people/2
thread-3  https://swapi.dev/api/people/3
...
...
thread-10  https://swapi.dev/api/people/10

"""


def get_urls():
    urls = []
    for i in range(1, 11):
        magic_url = f"https://swapi.dev/api/people/{i}"
        urls.append(magic_url)
    return urls


def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data.get("name")


@timeit
def main():
    """

   Returns:

   NOTE:
       ThreadPool object can be created with whatever number of threads
       we would like.
       For example, `pool = ThreadPool(100)`

       `pool` object has `map` method which distributes the collection elements
       across available threads in pool.

       `pool.map()` function returns a list object

   """
    pool_size = 10
    pool = ThreadPool(10)
    breakpoint()
    urls = get_urls()
    results = pool.map(fetch_data, urls)

    print(results)


if __name__ == "__main__":
    main()
