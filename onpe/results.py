from onpe.requests import get_response

base_url = "https://api.resultadoserm2022.onpe.gob.pe/results"
# codes
regional_governor = "01"
regional_council = "02"
province = "03"
district = "04"


def regional_governor_results(ubigeo: str) -> dict:
    url = f"{base_url}/{regional_governor}/{ubigeo}"
    return get_response(url)


def regional_council_results(ubigeo: str) -> dict:
    url = f"{base_url}/{regional_council}/{ubigeo}"
    return get_response(url)


def provincial_results(ubigeo: str) -> dict:
    url = f"{base_url}/{province}/{ubigeo}"
    return get_response(url)


def district_results(ubigeo: str) -> dict:
    url = f"{base_url}/{district}/{ubigeo}"
    return get_response(url)
