from hamcrest import assert_that, equal_to


def check_equal(actual, expected):
    """
    Asserts that the actual value is equal to the expected value.

    :param actual: The actual value.
    :param expected: The expected value to compare against.
    """

    assert_that(actual, equal_to(expected))


def check_count_output(output: list, expected_count: int):
    """
    Asserts that the length of the output list matches the expected count.

    :param output: A list representing output lines.
    :param expected_count: The expected number of output lines.
    """

    assert_that(len(output), equal_to(expected_count))
