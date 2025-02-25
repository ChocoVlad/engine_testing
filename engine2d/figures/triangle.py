from checkers.figure_checker import validate_triangle_vertices
from engine2d.figures.base_figure import BaseFigure


class Triangle(BaseFigure):
    """Represents a triangle figure for rendering."""

    def __init__(self, corner_vertices: list, engine):
        """
        Initializes a Triangle instance.

        :param corner_vertices: A list of vertices defining the triangle.
        :param engine: The rendering engine instance.
        """

        super().__init__(engine)
        validate_triangle_vertices(corner_vertices)
        self.corner_vertices = corner_vertices
        self.draw_text = f'Drawing Triangle: {", ".join(map(str, self.corner_vertices))} vertices'
