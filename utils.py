import json


def load_json(file_name):
    with open(file_name, "r") as json_file:
        database = json.load(json_file)
    
    return database


def dump_json(filename, database):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(database, json_file, ensure_ascii=False, indent=4)


def to_snake_case(column_name):
    return '_'.join(column_name.split()).lower()


def find_medicine(query, choices, threshold=80):
    """
    Find the best match for a query in the specified field of the data.
    :param query: The user's input.
    :param data: The DataFrame containing medicine information.
    :param field: The field to search in ('name_of_medicinal_product' or 'active_substance').
    :param threshold: The similarity threshold.
    :return: The best match if above the threshold, else None.
    """

    best_match, similarity = process.extractOne(query, choices)
    if similarity >= threshold:
        return best_match
    else:
        return None



def find_closest_match(query, choices):
    """
    Find the closest match for a query in a list of choices based on Levenshtein distance.
    :param query: The user's input.
    :param choices: A list of possible choices (e.g., medicine names or active substances).
    :return: The closest match.
    """
    closest_match = None
    shortest_distance = float('inf')

    for choice in choices:
        distance = lev.distance(query.lower(), choice.lower())
        if distance < shortest_distance:
            shortest_distance = distance
            closest_match = choice

    return closest_match