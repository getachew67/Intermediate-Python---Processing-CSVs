
import pandas as pd


def parse(file_name):
    """
    Utilizes pandas to read in a .CSV file and create a dataframe which can be
    manipulated using tools in the pandas library.
    """
    return pd.read_csv(file_name)


def species_count(info):
    """
    Takes the parsed data set created by the parse function and counts the
    number of unique species in the file. The method then takes the length and
    returns its value.
    """
    return len(info.loc[:, 'name'].unique())


def max_level(info):
    """
    Takes the parsed data set created by the parse function and finds the
    species that has the highest level given the data. The method returns a
    tuple which contains the species name and level of the highest leveled
    species.
    """
    value = info.loc[info['level'].idxmax()]
    return value['name'], value['level']


def filter_range(info, lower, upper):
    """
    Takes the parsed data set given by the parse function and lower and upper
    restrictions for the level to filter out any Pokemon that do not fall
    within the given range.  The range is lower inclusive and upper exclusive.
    This method returns a list of the names of the Pokemon who's level falls
    within the range.
    """
    in_range = info[(info['level'] >= lower) & (info['level'] < upper)]
    result = []
    for i in in_range['name']:
        i = i.strip()
        if len(i):
            result.append(i)
    return result


def mean_attack_for_type(info, p_type):
    """
    Takes the parsed data set given by the parse function and a string variable
    for the type of Pokemon we are interested in.  Using this information, the
    method sums the attack values and total count of Pokemon which match the
    type we are interested in.  The method returns None if no Pokemon in the
    data set match the specified type and the average of their attack values if
    matching type Pokemon are found.
    """
    return info[(info['type'] == p_type)].loc[:, 'atk'].mean()


def count_types(info):
    """
    This takes the data set given by the parse function and creates a
    dictionary that different types of Pokemon found and number of each type
    in the data.  The method returns the dictionary with each type found and
    the count of each.
    """
    return dict(info.groupby('type')['type'].count())


def highest_stage_per_type(info):
    """
    This takes the parsed data set given by the parse function and sorts out
    each Pokemon type included in the data and what the highest stage is for
    that type.  This method returns a dictionary with the type and max stage
    for each type in the data.
    """
    return dict(info.groupby('type')['stage'].max())


def mean_attack_per_type(info):
    """
    This takes in the parsed data set given by the parse function finds the
    average attack value for each Pokemon type present in the data.  This
    method returns a dictionary containing each type and its corresponding
    average attack value.
    """
    return dict(info.groupby('type')['atk'].mean())
