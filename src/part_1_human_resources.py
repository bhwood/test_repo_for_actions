from copy import deepcopy


def make_name_tags(guest_list: list[dict]) -> list[dict]:
    updated_list = deepcopy(guest_list)
    for guest in updated_list:
        name_tag = f"{guest['title']} {guest['forename']} {guest['surname']}, {guest['company']}"
        guest["name_tag"] = name_tag
    return updated_list


def create_poll(poll_data: list) -> dict:
    result = {}
    for item in poll_data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
