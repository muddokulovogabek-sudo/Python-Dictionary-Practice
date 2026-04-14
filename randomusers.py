from dataset import randomuser_data


def get_full_names(data: dict) -> list[str]:
    result = []
    for user in data["results"]:
        full_name = user["name"]["first"] + " " + user["name"]["last"]
        result.append(full_name)
    return result


def get_users_by_country(data: dict, country: str) -> list[dict]:
    result = []
    for user in data["results"]:
        if user["location"]["country"] == country:
            result.append({
                "name": user["name"]["first"] + " " + user["name"]["last"],
                "email": user["email"]
            })
    return result


def count_users_by_gender(data: dict) -> dict:
    result = {}
    for user in data["results"]:
        gender = user["gender"]
        if gender in result:
            result[gender] += 1
        else:
            result[gender] = 1
    return result


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    result = []
    for user in data["results"]:
        if user["dob"]["age"] > age:
            result.append(user["email"])
    return result


def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    sorted_users = sorted(
        data["results"],
        key=lambda user: user["dob"]["age"],
        reverse=descending
    )

    result = []
    for user in sorted_users:
        result.append({
            "name": user["name"]["first"] + " " + user["name"]["last"],
            "age": user["dob"]["age"]
        })
    return result


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    result = []
    for user in data["results"]:
        username = user["login"]["username"]
        if username.startswith(letter):
            result.append(username)
    return result


def get_average_age(data: dict) -> float:
    total = 0
    count = 0

    for user in data["results"]:
        total += user["dob"]["age"]
        count += 1

    return total / count if count > 0 else 0


def group_users_by_nationality(data: dict) -> dict:
    result = {}
    for user in data["results"]:
        nat = user["nat"]
        if nat in result:
            result[nat] += 1
        else:
            result[nat] = 1
    return result


def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    result = []
    for user in data["results"]:
        lat = user["location"]["coordinates"]["latitude"]
        lon = user["location"]["coordinates"]["longitude"]
        result.append((lat, lon))
    return result


def get_oldest_user(data: dict) -> dict:
    oldest = data["results"][0]

    for user in data["results"]:
        if user["dob"]["age"] > oldest["dob"]["age"]:
            oldest = user

    return {
        "name": oldest["name"]["first"] + " " + oldest["name"]["last"],
        "age": oldest["dob"]["age"],
        "email": oldest["email"]
    }


def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    result = []
    for user in data["results"]:
        if user["location"]["timezone"]["offset"] == offset:
            result.append({
                "name": user["name"]["first"] + " " + user["name"]["last"],
                "city": user["location"]["city"]
            })
    return result


def get_registered_before_year(data: dict, year: int) -> list[dict]:
    result = []
    for user in data["results"]:
        reg_year = int(user["registered"]["date"][:4])
        if reg_year < year:
            result.append({
                "name": user["name"]["first"] + " " + user["name"]["last"],
                "registered": user["registered"]["date"][:10]
            })
    return result


# TEST
result = get_full_names(randomuser_data)
print(result)