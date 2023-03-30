import os

import pandas as pd

from onpe.results import provincial_results
from onpe.ubigeos import provincial_ubigeos
from scripts.common.results_by_political_party import \
    results_by_political_party
from scripts.common.ubigeos import order_ubigeos, get_parent

blank_votes = "80"
voided_votes = "81"

proj_path = f"{os.path.dirname(__file__)}/.."


def get_provincial_winner_by_district(province_code: str):
    division_map = order_ubigeos(provincial_ubigeos())

    department_code = get_parent(province_code)
    province: dict[str, str | dict] = \
        division_map[department_code]["provinces"][province_code]
    districts: dict[str, dict[str, str]] = province["districts"]

    winner_by_district: list[dict] = []

    for ubigeo, name_dict in districts.items():
        _, _, district_results = \
            results_by_political_party(provincial_results(ubigeo))

        district_results.pop(blank_votes)
        district_results.pop(voided_votes)

        results_as_list: list[dict] = list(district_results.items())
        results_as_list.sort(key=lambda party: party[1]["votes"], reverse=True)

        winner: dict[str, str | int] = results_as_list[0][1]
        winner = {"ubigeo": ubigeo, "district": districts[ubigeo]["name"],
                  **winner}

        winner_by_district.append(winner)

    results_dataframe = pd.DataFrame(winner_by_district)

    results_dataframe.to_csv(
        f"{proj_path}/output/"
        f"results_by_districts_{province['name']}_{province_code}.csv",
        index=False
    )
