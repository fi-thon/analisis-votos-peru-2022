import time
from typing import Any, Callable

import requests
from requests import Response

DEFAULT_MAX_ATTEMPTS = 5
DEFAULT_MAX_TIMEOUT = 5


def execute_with_retries(f: Callable, args: dict = None,
                         max_attempts: int = DEFAULT_MAX_ATTEMPTS) -> Any:
    total_attempts = 0

    while total_attempts < max_attempts:
        try:
            if args:
                return f(**args)
            else:
                return f()
        except requests.Timeout:
            total_attempts += 1
            if total_attempts < max_attempts:
                time.sleep((2 ** total_attempts) / 10)
            else:
                return None


def get_response(url: str,
                 timeout: int = DEFAULT_MAX_TIMEOUT,
                 max_attempts: int = DEFAULT_MAX_ATTEMPTS) -> dict:

    print(f"obteniendo datos desde {url}")

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) "
                             "Gecko/20100101 Firefox/105.0"}
    request_params = {"url": url, "timeout": timeout, "headers": headers}
    response: Response | None = execute_with_retries(f=requests.get,
                                                     args=request_params,
                                                     max_attempts=max_attempts)

    if isinstance(response, Response):
        return response.json()
    else:
        return {}
