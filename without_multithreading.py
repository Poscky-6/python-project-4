import requests
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[ INFO ] total time to execute :: {end}")
        return result

    return wrapper


@timeit
def main():
    final = []
    for i in range(11):
        magic_url = f"https://swapi.dev/api/people/{i}"
        response = requests.get(magic_url)
        data = response.json()
        char_name = data.get("name")
        final.append(char_name)

    print(final)


if __name__ == "__main__":
    main()
