def assert_equal(actual, expected):
    """
    assert if it is equal
    :param actual:
    :param expected:
    :return:
    """
    try:
        assert actual == expected
        print("assert successful,actual value：{} is equal to expected value：{}".format(actual, expected))
    except AssertionError:
        print("assert fail,actual value：{} isn't equal to expected value：{}".format(actual, expected))
        raise AssertionError


def assert_true(*actual):
    """
    assert if it is true
    :param actual:
    :return:
    """
    try:
        assert actual[0] is True
        print("assert successful,actual value：{} is true".format(actual))
    except AssertionError:
        print("assert fail,actual value：{} is false".format(actual))
        raise AssertionError


def assert_in(actual, expected):
    """
    assert if contains text
    :param content: contains text
    :param target: target text
    :return:
    """
    try:
        assert actual in expected
        print("assert successful,target texts：{} contains texts：{}".format(actual, expected))
    except AssertionError:
        print("assert fail,target texts：{} don't contain texts：{}".format(actual, expected))
        raise AssertionError
