import requests
from mytoken import CTOKEN


def get(url, params=None):
    print(f"***GET*** {url}")
    response = requests.get(
        url,
        params=params,
        headers={
            "X-Kite-Version": "3",
            "Authorization": f"enctoken {CTOKEN}"
        },
    )

    return response
