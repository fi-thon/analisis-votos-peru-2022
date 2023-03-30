from argparse import Namespace

from config import parse_arguments
from scripts import get_provincial_winner_by_district


def execute_script(
    script_code: str,
    ubigeo: str = None,
    political_party_code: str = None,
):
    
    match script_code:
        case "provincial":
            get_provincial_winner_by_district(ubigeo)
        case _:
            print("No existe el 'script' buscado.")


if __name__ == "__main__":
    arguments: Namespace = parse_arguments()
    execute_script(
        script_code=arguments.script,
        ubigeo=arguments.ubigeo,
        political_party_code=arguments.partido,
    )
