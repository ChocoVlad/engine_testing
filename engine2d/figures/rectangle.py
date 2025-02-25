from engine2d.figures.base_figure import BaseFigure


class Rectangle(BaseFigure):
    """Represents a rectangle figure for rendering."""

    def __init__(self, start_point: tuple, width: int, height: int, engine):
        """
        Initializes a Rectangle instance.

        :param start_point: A tuple representing the starting coordinate of the rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param engine: The rendering engine instance.
        """

        super().__init__(engine)
        self.start_point = start_point
        self.width = width
        self.height = height
        self.draw_text = f'Drawing Rectangle: {self.start_point} with width {self.width} and height {self.height}'
