class BaseFigure:
    """BaseFigure is the abstract base class."""

    def __init__(self, engine):
        """
        Initializes a BaseFigure instance.

        :param engine: The rendering engine instance.
        """

        self.engine = engine
        self.draw_text = None

    def prepare_color_text(self) -> str:
        """
        Prepares the color text suffix.

        :return: Color text suffix.
        """

        figure_color = getattr(self.engine, 'current_color')
        color_text = f' in color {figure_color}' if figure_color else ''
        return color_text

    def draw(self):
        """Prints the complete drawing text, which includes the figure's text and its color."""

        print(f'{self.draw_text}{self.prepare_color_text()}')


class StubFigure:
    """A stub implementation of a figure."""

    def draw(self):
        """Prints a fixed output 'Done'."""

        print('Done')
