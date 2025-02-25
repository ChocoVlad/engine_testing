import allure
from checkers.test_checker import check_equal
from engine2d.engine import Engine2D
from engine2d.figures.triangle import Triangle
from engine2d.figures.circle import Circle
from engine2d.figures.rectangle import Rectangle
from helpers.output_helper import prepare_output


@allure.feature("Triangle Integration")
@allure.story("Test triangle drawing with tuple vertices")
def test_triangle_integration(capsys):
    with allure.step("Prepare expected output"):
        expected = "Drawing Triangle: (1, 2), (2, 3), (3, 4) vertices in color blue"
    with allure.step("Create engine and triangle"):
        engine = Engine2D(initial_color="blue")
        triangle = Triangle([(1, 2), (2, 3), (3, 4)], engine)
    with allure.step("Draw triangle"):
        triangle.draw()
    with allure.step("Capture and verify output"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected)


@allure.feature("Circle Integration")
@allure.story("Test circle drawing")
def test_circle_integration(capsys):
    with allure.step("Prepare expected output"):
        expected = "Drawing Circle: (0, 0) with radius 5 in color red"
    with allure.step("Create engine and circle"):
        engine = Engine2D(initial_color="red")
        circle = Circle((0, 0), 5, engine)
    with allure.step("Draw circle"):
        circle.draw()
    with allure.step("Capture and verify output"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected)


@allure.feature("Rectangle Integration")
@allure.story("Test rectangle drawing")
def test_rectangle_integration(capsys):
    with allure.step("Prepare expected output"):
        expected = "Drawing Rectangle: (2, 3) with width 15 and height 25 in color green"
    with allure.step("Create engine and rectangle"):
        engine = Engine2D(initial_color="green")
        rectangle = Rectangle((2, 3), 15, 25, engine)
    with allure.step("Draw rectangle"):
        rectangle.draw()
    with allure.step("Capture and verify output"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected)


@allure.feature("Engine Color Update Integration")
@allure.story("Test figure updates its color after engine color change")
def test_figure_color(capsys):
    with allure.step("Prepare expected outputs"):
        expected_before = "Drawing Circle: (0, 0) with radius 5 in color black"
        expected_after = "Drawing Circle: (0, 0) with radius 5 in color red"
    with allure.step("Create engine and circle with initial color"):
        engine = Engine2D(initial_color="black")
        circle = Circle((0, 0), 5, engine)
    with allure.step("Draw circle with initial color and verify output"):
        circle.draw()
        output_before = prepare_output(capsys)[0]
        check_equal(output_before, expected_before)
    with allure.step("Change engine color and draw circle again"):
        engine.change_color("red")
        circle.draw()
        output_after = prepare_output(capsys)[0]
        check_equal(output_after, expected_after)
