from engine2d.figures.base_figure import BaseFigure


class Circle(BaseFigure):
    """Represents a circle figure for rendering."""

    def __init__(self, start_point: tuple, radius: int, engine):
        """
        Initializes a Circle instance.

        :param start_point: A tuple representing the center coordinate of the circle.
        :param radius: The radius of the circle.
        :param engine: The rendering engine instance.
        """
        super().__init__(engine)
        self.start_point = start_point
        self.radius = radius
        self.draw_text = f'Drawing Circle: {self.start_point} with radius {self.radius}'
