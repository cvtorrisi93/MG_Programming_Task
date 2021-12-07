from loganalyser import get_info


def test_get_info():
    test_dict = {}

    test_string = "abacbcdaebbbacabdee"
    for character in test_string:
        test_dict = get_info(test_dict, character)

    assert test_dict == {'a': 5, 'b': 6, 'c': 3, 'd': 2, 'e': 3}


if __name__ == "__main__":
    test_get_info()
    print("test_get_info() has passed!")
