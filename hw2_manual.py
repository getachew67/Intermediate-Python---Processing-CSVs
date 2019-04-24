
def parse(file_name, int_cols):
    """
    Parses the CSV file specified by file_name and returns the data as a list
    of dictionaries where each row is represented by a dictionary that
    has keys for each column and value which is the entry for that column
    at that row.

    Also takes a list of column names that should have the data for that column
    converted to integers. All other data will be str.
    """
    data = []
    with open(file_name) as f:
        headers = f.readline().strip().split(',')
        num_cols = len(headers)

        for line in f.readlines():
            row_data = line.strip().split(',')
            row = {}
            for i in range(num_cols):
                if headers[i] in int_cols:
                    row[headers[i]] = int(row_data[i])
                else:
                    row[headers[i]] = row_data[i]
            data.append(row)
    return data


def species_count(info):
    """
    Takes the parsed data set created by the parse function and counts the
    number of unique species in the file utilizing a set to avoid duplicates.
    The method then takes the length of the set and returns its value.
    """
    species = set()
    for i in info:
        x = i['name']
        species.add(x)
    return len(species)


def max_level(info):
    """
    Takes the parsed data set created by the parse function and finds the
    species that has the highest level given the data. The method returns a
    tuple which contains the species name and level of the highest leveled
    species.
    """
    level = 0
    species = ''
    for i in info:
        if i['level'] > level:
            level = i['level']
            species = i['name']
    result = (species, level)
    return result


def filter_range(info, lower, upper):
    """
    Takes the parsed data set given by the parse function and lower and upper
    restrictions for the level to filter out any Pokemon that do not fall
    within the given range.  The range is lower inclusive and upper exclusive.
    This method returns a list of the names of the Pokemon who's level falls
    within the range.
    """
    in_range = list()
    for i in info:
        if i['level'] in range(lower, upper):
            in_range.append(i['name'])
    return in_range


def mean_attack_for_type(info, p_type):
    """
    Takes the parsed data set given by the parse function and a string variable
    for the type of Pokemon we are interested in.  Using this information, the
    method sums the attack values and total count of Pokemon which match the
    type we are interested in.  The method returns None if no Pokemon in the
    data set match the specified type and the average of their attack values if
    matching type Pokemon are found.
    """
    count = 0
    total = 0
    for i in info:
        if i['type'] == p_type:
            count += 1
            total = total + i['atk']
    if count == 0:
        return None
    else:
        return total/count


def count_types(info):
    """
    This takes the data set given by the parse function and creates a
    dictionary that different types of Pokemon found and number of each type
    in the data.  The method returns the dictionary with each type found and
    the count of each.
    """
    types = {}
    for i in info:
        if i['type'] in types:
            types[i['type']] += 1
        else:
            types[i['type']] = 1
    return types


def highest_stage_per_type(info):
    """
    This takes the parsed data set given by the parse function and sorts out
    each Pokemon type included in the data and what the highest stage is for
    that type.  This method returns a dictionary with the type and max stage
    for each type in the data.
    """
    max_stages = {}
    for i in info:
        if i['type'] in max_stages:
            if i['stage'] > max_stages[i['type']]:
                max_stages[i['type']] = i['stage']
        else:
            max_stages[i['type']] = i['stage']
    return max_stages


def mean_attack_per_type(info):
    """
    This takes in the parsed data set given by the parse function finds the
    average attack value for each Pokemon type present in the data.  This
    method returns a dictionary containing each type and its corresponding
    average attack value.
    """
    types = {}
    attacks = {}
    results = {}
    for i in info:
        if i['type'] in types:
            types[i['type']] += 1
        else:
            types[i['type']] = 1
    for i in info:
        if i['type'] in attacks:
            attacks[i['type']] += i['atk']
        else:
            attacks[i['type']] = i['atk']
    for k in attacks:
        avg = attacks[k] / types[k]
        results[k] = avg
    return results
