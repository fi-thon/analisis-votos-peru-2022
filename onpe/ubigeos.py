from onpe.common import base_url
from onpe.requests import get_response

base_url = f"{base_url}/ubigeos"
# codes
regional_governor = "01"
regional_council = "02"
province = "03"
district = "04"


def regional_governor_ubigeos() -> dict:
    url = f"{base_url}/{regional_governor}"
    return get_response(url)


def regional_council_ubigeos() -> dict:
    url = f"{base_url}/{regional_council}"
    return get_response(url)


def provincial_ubigeos() -> dict:
    url = f"{base_url}/{province}"
    return get_response(url)


def district_ubigeos() -> dict:
    url = f"{base_url}/{district}"
    return get_response(url)
