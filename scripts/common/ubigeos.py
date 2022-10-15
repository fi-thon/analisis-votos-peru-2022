# parent node
parent_key = "CDGO_PADRE"
# departments
department_code_key = "CDGO_DEP"
department_name_key = "DESC_DEP"
# provinces
province_code_key = "CDGO_PROV"
province_name_key = "DESC_PROV"
# districts
district_code_key = "CDGO_DIST"
district_name_key = "DESC_DIST"


def get_parent(division_code: str) -> str:
    department: str = division_code[:2]
    province: str = division_code[2:4]
    district: str = division_code[4:]

    if district != "00":
        return department + province + "00"
    elif province != "00":
        return department + "0000"
    else:
        return "000000"


def order_ubigeos(ubigeos_dict: dict) -> dict[str, dict[str, str | dict]]:
    departments: list[dict[str, str]] = ubigeos_dict["departments"]
    provinces: list[dict[str, str]] = ubigeos_dict["provinces"]
    districts: list[dict[str, str]] = ubigeos_dict["districts"]

    division_map = {}

    department: dict[str, str | dict]
    for department in departments:
        department_name: str = department[department_name_key]
        department_code: str = department[department_code_key]

        division_map[department_code] = {
            "name": department_name,
            "provinces": {}
        }

    province: dict[str, str | dict]
    for province in provinces:
        province_name: str = province[province_name_key]
        province_code: str = province[province_code_key]
        parent_code: str = province[parent_key]

        division_map[parent_code]["provinces"][province_code] = {
            "name": province_name,
            "districts": {}
        }

    district: dict[str, str | dict]
    for district in districts:
        district_name: str = district[district_name_key]
        district_code: str = district[district_code_key]
        province_code: str = district[parent_key]
        department_code: str = get_parent(province_code)

        # having "000000" as its parent's code means it is actually a province
        if department_code != "000000":
            province = division_map[department_code]["provinces"][
                province_code]
            province["districts"][district_code] = {"name": district_name}

    return division_map
