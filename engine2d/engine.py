class Engine2D:
    """The Engine2D class represents a 2D rendering engine for drawing figures."""

    def __init__(self, initial_color="black"):
        """
        Initializes an instance of Engine2D.

        :param initial_color: The initial color for the figures.
        """
        self.canvas = []
        self.current_color = initial_color

    def add_figure(self, figure):
        """
        Adds a figure to the canvas.

        :param figure: An object representing a figure.
        """
        self.canvas.append(figure)

    def change_color(self, new_color):
        """
        Changes the current color of the engine.

        :param new_color: The new color to be applied to the figures.
        """
        self.current_color = new_color

    def draw(self):
        """Calls the draw() method of each figure on the canvas and then clears the canvas."""
        for figure in self.canvas:
            figure.draw()
        self.canvas.clear()


class StubEngine:
    """A stub implementation of the Engine2D."""
    current_color = "red"
