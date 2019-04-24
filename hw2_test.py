from cse163_utils import assert_equals
# Don't worry about this import syntax, we will talk about it later

import hw2_manual
import hw2_pandas

# Parse .csv files into dataframes using parse function from Part 1 - Pandas
NUMERICAL_COLS = ['id', 'level', 'atk', 'def', 'hp', 'stage']
data_m1 = hw2_manual.parse('pokemon_test.csv', NUMERICAL_COLS)
data_m2 = hw2_manual.parse('pokemon_box.csv', NUMERICAL_COLS)

# Parse .csv files into dataframes using parse function from Part 1 - Pandas
data_p1 = hw2_pandas.parse('pokemon_test.csv')
data_p2 = hw2_pandas.parse('pokemon_box.csv')


def test_species_count():
    """
    Tests the output of both versions of species_count() function.
    """

    # Test Part 0 - Manual
    print('Test species_count from Part 0 - Manual')

    assert_equals(3, hw2_manual.species_count(data_m1))
    assert_equals(82, hw2_manual.species_count(data_m2))

    # Test Part 1 - Pandas
    print('Test species_count from Part 1 - Pandas')

    assert_equals(3, hw2_pandas.species_count(data_p1))
    assert_equals(82, hw2_pandas.species_count(data_p2))


def test_max_level():
    """
    Tests the output of both versions of max_level() function.
    """

    # Test Part 0 - Manual
    print('Test max_level from Part 0 - Manual')

    assert_equals(('Lapras', 72), hw2_manual.max_level(data_m1))
    assert_equals(('Victreebel', 100), hw2_manual.max_level(data_m2))

    # Test Part 1 - Pandas
    print('Test max_level from Part 1 - Pandas')

    assert_equals(('Lapras', 72), hw2_pandas.max_level(data_p1))
    assert_equals(('Victreebel', 100), hw2_pandas.max_level(data_p2))


def test_filter_range():
    """
    Tests the output of both versions of filter_range() function.
    """
    answer_1 = ['Arcanine', 'Arcanine', 'Starmie']
    answer_2 = (['Metapod', 'Caterpie', 'Ninetales', 'Weezing', 'Tangela',
                'Butterfree', 'Arcanine'])

    # Test Part 0 - Manual
    print('Test filter_range from Part 0 - Manual')

    assert_equals(answer_1, hw2_manual.filter_range(data_m1, 30, 70))
    assert_equals(answer_2, hw2_manual.filter_range(data_m2, 1, 9))

    # Test Part 1 - Pandas
    print('Test filter_range from Part 1 - Pandas')

    assert_equals(answer_1, hw2_pandas.filter_range(data_p1, 30, 70))
    assert_equals(answer_2, hw2_pandas.filter_range(data_p2, 1, 9))


def test_mean_attack_for_type():
    """
    Tests the output of both versions of mean_attack_for_type() function.
    """

    # Test Part 0 - Manual
    print('Test mean_attack_for_type from Part 0 - Manual')

    assert_equals(47.5, hw2_manual.mean_attack_for_type(data_m1, 'fire'))
    assert_equals(99.4, hw2_manual.mean_attack_for_type(data_m2, 'fire'))

    # Test Part 1 - Pandas
    print('Test mean_attack_for_type from Part 1 - Pandas')

    assert_equals(47.5, hw2_pandas.mean_attack_for_type(data_p1, 'fire'))
    assert_equals(99.4, hw2_pandas.mean_attack_for_type(data_p2, 'fire'))


def test_count_types():
    """
    Tests the output of both versions of count_types() function.
    """
    answer_2 = ({'normal': 10, 'fire': 15, 'water': 24, 'fighting': 3,
                'grass': 17, 'poison': 12, 'bug': 3, 'fairy': 3, 'psychic': 6,
                 'rock': 7, 'flying': 6, 'ghost': 3, 'ground': 5,
                 'electric': 1})

    # Test Part 0 - Manual
    print('Test count_types from Part 0 - Manual')

    assert_equals({'fire': 2, 'water': 2}, hw2_manual.count_types(data_m1))
    assert_equals(answer_2, hw2_manual.count_types(data_m2))

    # Test Part 1 - Pandas
    print('Test count_types from Part 1 - Pandas')

    assert_equals({'fire': 2, 'water': 2}, hw2_pandas.count_types(data_p1))
    assert_equals(answer_2, hw2_pandas.count_types(data_p2))


def test_highest_stage_per_type():
    """
    Tests the output of both versions of highest_stage_per_type() function.
    """
    answer_1 = {'fire': 2, 'water': 2}
    answer_2 = ({'normal': 2, 'fire': 3, 'water': 2, 'fighting': 2, 'grass': 3,
                'poison': 3, 'bug': 3, 'fairy': 1, 'psychic': 3, 'rock': 3,
                 'flying': 3, 'ghost': 3, 'ground': 2, 'electric': 1})

    # Test Part 0 - Manual
    print('Test highest_stage_per_type from Part 0 - Manual')

    assert_equals(answer_1, hw2_manual.highest_stage_per_type(data_m1))
    assert_equals(answer_2, hw2_manual.highest_stage_per_type(data_m2))

    # Test Part 1 - Pandas
    print('Test highest_stage_per_type from Part 1 - Pandas')

    assert_equals(answer_1, hw2_pandas.highest_stage_per_type(data_p1))
    assert_equals(answer_2, hw2_pandas.highest_stage_per_type(data_p2))


def test_mean_attack_per_type():
    """
    Tests the output of both versions of mean_attack_per_type() function.
    """
    answer_1 = {'water': 140.5, 'fire': 47.5}
    answer_2 = ({'normal': 108.0, 'fire': 99.4, 'water': 99.75,
                'fighting': 99.66666666666667, 'grass': 105.3529411764706,
                 'poison': 121.75, 'bug': 25.0, 'fairy': 76.33333333333333,
                 'psychic': 114.83333333333333, 'rock': 84.85714285714286,
                 'flying': 110.83333333333333, 'ghost': 88.0, 'ground': 116.6,
                 'electric': 64.0})

    # Test Part 0 - Manual
    print('Test mean_attack_per_type from Part 0 - Manual')

    assert_equals(answer_1, hw2_manual.mean_attack_per_type(data_m1))
    assert_equals(answer_2, hw2_manual.mean_attack_per_type(data_m2))

    # Test Part 1 - Pandas
    print('Test mean_attack_per_type from Part 1 - Pandas')

    assert_equals(answer_1, hw2_pandas.mean_attack_per_type(data_p1))
    assert_equals(answer_2, hw2_pandas.mean_attack_per_type(data_p2))


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_types()
    test_highest_stage_per_type()
    test_mean_attack_per_type()


if __name__ == '__main__':
    main()
