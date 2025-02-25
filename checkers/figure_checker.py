from hamcrest import assert_that, equal_to


def validate_triangle_vertices(vertices):
    """
    Validates that the triangle has exactly three vertices.

    :param vertices: A list of vertices.
    """

    assert_that(len(vertices), equal_to(3))
