from scripts.common.parsing import parse_int

results_key = "results"
summary_key = "generals"
general_data_key = "generalData"

# results
political_party_id_key = "C_CODI_AGP"
political_party_name_key = "AGRUPACION"
votes_key = "TOTAL_VOTOS"
percentage_valid_key = "POR_VALIDOS"
percentage_total_key = "POR_EMITIDOS"

# general
total_voters_key = "ELECTORES_HABIL"
actual_voters_key = "TOT_CIUDADANOS_VOTARON"


def results_by_political_party(
        election_results: dict
) -> tuple[int, int, dict[str, dict[str, int | str]]]:

    election_results_by_party = election_results[results_key]
    summary = election_results[summary_key][general_data_key]
    political_parties: dict[str, dict[str, str | int]] = {}

    total_voters: int = parse_int(summary[total_voters_key])
    actual_voters: int = parse_int(summary[actual_voters_key])

    political_party_results: dict[str, str]
    for political_party_results in election_results_by_party:
        political_party_id: str = political_party_results.get(
            political_party_id_key)

        if political_party_id:

            political_party_name: str = political_party_results.get(
                political_party_name_key)

            political_party_total_votes: int = parse_int(
                political_party_results.get(votes_key) or "0"
            )

            political_party_percentage_valid: float = float(
                political_party_results.get(percentage_valid_key) or "0.0"
            )

            political_party_percentage_total: float = float(
                political_party_results.get(percentage_total_key) or "0.0"
            )

            political_parties[political_party_id] = {
                "name": political_party_name,
                "votes": political_party_total_votes,
                "percentage_valid": political_party_percentage_valid,
                "percentage_total": political_party_percentage_total
            }

    return total_voters, actual_voters, political_parties
