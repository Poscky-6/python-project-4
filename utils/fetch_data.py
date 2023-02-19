"""
uses HTTP GET request to fetch any resource data from a given URL endpoint
"""
import logging
import requests
from typing import List, Dict, Union
from requests import Response

# logging configuration
logging.basicConfig(
    filename="utils/example.log",
    encoding="utf-8",
    level=logging.INFO
)


def mylogger(func):
    def wrapper(url, **kwargs):
        try:
            logging.info(f"we are hitting - {url}")
            result_ = func(url)
            logging.info(f"success - {result_.status_code}")
        except Exception:
            logging.error("there are issues in fetching details")

        return result_

    return wrapper


@mylogger
def hit_url(url: str) -> Response:
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    else:
        return response


def fetch_data(urls: List) -> Union[List, Dict]:
    """fetches data from given urls"""

    data = []
    for url in urls:
        res = requests.get(url)
        data.append(res.json())

    return data