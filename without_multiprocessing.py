"""
whenever we are doing compute intensive operation - multi-processing

"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"[ INFO ] total time to execute :: {end}")
        return result

    return wrapper


def some_heavy_work(range_):
    return [i ** 2 for i in range(range_)]


@timeit
def main():
    ranges = [100000001, 100000002, 100000003, 100000004, 100000005, 100000006,
              100000071, 100000042, 100000053, 100000024, 100000035, 100000016]

    for range_ in ranges:
        some_heavy_work(range_)


if __name__ == "__main__":
    main()



