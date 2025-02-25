from checkers.test_checker import check_equal
from engine2d.engine import StubEngine
from engine2d.figures.circle import Circle
from engine2d.figures.rectangle import Rectangle
from engine2d.figures.triangle import Triangle
from helpers.output_helper import prepare_output
import allure


@allure.feature("Figure Unit Tests")
@allure.story("Triangle draw text")
def test_triangle_draw_text():
    with allure.step("Prepare expected draw text"):
        expected_text = "Drawing Triangle: (1, 2), (2, 3), (3, 4) vertices"
    with allure.step("Create StubEngine and Triangle"):
        engine = StubEngine()
        triangle = Triangle([(1, 2), (2, 3), (3, 4)], engine)
    with allure.step("Verify triangle draw text"):
        check_equal(triangle.draw_text, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Circle draw text")
def test_circle_draw_text():
    with allure.step("Prepare expected draw text"):
        expected_text = "Drawing Circle: (0, 0) with radius 5"
    with allure.step("Create StubEngine and Circle"):
        engine = StubEngine()
        circle = Circle((0, 0), 5, engine)
    with allure.step("Verify circle draw text"):
        check_equal(circle.draw_text, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Rectangle draw text")
def test_rectangle_draw_text():
    with allure.step("Prepare expected draw text"):
        expected_text = "Drawing Rectangle: (2, 3) with width 15 and height 25"
    with allure.step("Create StubEngine and Rectangle"):
        engine = StubEngine()
        rectangle = Rectangle((2, 3), 15, 25, engine)
    with allure.step("Verify rectangle draw text"):
        check_equal(rectangle.draw_text, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Triangle draw")
def test_triangle_draw(capsys):
    with allure.step("Prepare expected printed text"):
        expected_text = "Drawing Triangle: (3, 4), (5, 6), (7, 8) vertices in color red"
    with allure.step("Create StubEngine and Triangle and call draw"):
        engine = StubEngine()
        triangle = Triangle([(3, 4), (5, 6), (7, 8)], engine)
        triangle.draw()
    with allure.step("Capture output and verify printed text"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Circle draw")
def test_circle_draw(capsys):
    with allure.step("Prepare expected printed text"):
        expected_text = "Drawing Circle: (0, 0) with radius 5 in color red"
    with allure.step("Create StubEngine and Circle and call draw"):
        engine = StubEngine()
        circle = Circle((0, 0), 5, engine)
        circle.draw()
    with allure.step("Capture output and verify printed text"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Rectangle draw")
def test_rectangle_draw(capsys):
    with allure.step("Prepare expected printed text"):
        expected_text = "Drawing Rectangle: (2, 3) with width 15 and height 25 in color red"
    with allure.step("Create StubEngine and Rectangle and call draw"):
        engine = StubEngine()
        rectangle = Rectangle((2, 3), 15, 25, engine)
        rectangle.draw()
    with allure.step("Capture output and verify printed text"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected_text)


@allure.feature("Figure Unit Tests")
@allure.story("Figure color text")
def test_figure_color_text():
    with allure.step("Prepare expected color text"):
        expected_text = " in color red"
    with allure.step("Create StubEngine and Circle, then get color text"):
        engine = StubEngine()
        circle = Circle((10, 23), 2, engine)
        actual_color_text = circle.prepare_color_text()
    with allure.step("Verify color text"):
        check_equal(actual_color_text, expected_text)
