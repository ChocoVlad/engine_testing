from checkers.test_checker import check_equal, check_count_output
from engine2d.engine import Engine2D
from engine2d.figures.triangle import Triangle
from engine2d.figures.circle import Circle
from engine2d.figures.rectangle import Rectangle
from helpers.output_helper import prepare_output
import allure


@allure.feature("Engine Integration")
@allure.story("Single figure drawing in the engine")
def test_single_figure_integration(capsys):
    with allure.step("Prepare expected output"):
        expected = "Drawing Circle: (5, 5) with radius 10 in color red"
    with allure.step("Create engine and circle"):
        engine = Engine2D(initial_color="red")
        circle = Circle((5, 5), 10, engine)
    with allure.step("Add figure to engine and draw"):
        engine.add_figure(circle)
        engine.draw()
    with allure.step("Capture and verify output"):
        captured = prepare_output(capsys)[0]
        check_equal(captured, expected)


@allure.feature("Engine Integration")
@allure.story("Multiple figures drawing in engine")
def test_multiple_figures_integration(capsys):
    with allure.step("Prepare expected outputs"):
        expected_triangle = "Drawing Triangle: (1, 2), (3, 4), (1, 2) vertices in color blue"
        expected_circle = "Drawing Circle: (0, 0) with radius 5 in color blue"
        expected_rectangle = "Drawing Rectangle: (2, 2) with width 8 and height 12 in color blue"
    with allure.step("Create engine and figures"):
        engine = Engine2D(initial_color="blue")
        triangle = Triangle([(1, 2), (3, 4), (1, 2)], engine)
        circle = Circle((0, 0), 5, engine)
        rectangle = Rectangle((2, 2), 8, 12, engine)
    with allure.step("Add figures to engine and draw"):
        engine.add_figure(triangle)
        engine.add_figure(circle)
        engine.add_figure(rectangle)
        engine.draw()
    with allure.step("Capture and verify output"):
        captured = prepare_output(capsys)
        check_count_output(captured, 3)
        check_equal(captured, [expected_triangle, expected_circle, expected_rectangle])


@allure.feature("Engine Integration")
@allure.story("Engine color change updates figure drawing")
def test_engine_color_change_integration(capsys):
    with allure.step("Prepare expected outputs"):
        expected1 = "Drawing Triangle: 4, 5, 6 vertices in color black"
        expected2 = "Drawing Circle: (1, 1) with radius 7 in color green"
    with allure.step("Create engine and add triangle with initial color"):
        engine = Engine2D(initial_color="black")
        triangle = Triangle([4, 5, 6], engine)
        engine.add_figure(triangle)
    with allure.step("Draw triangle and verify output"):
        engine.draw()
        captured1 = prepare_output(capsys)
        check_count_output(captured1, 1)
        check_equal(captured1[0], expected1)
    with allure.step("Change engine color and add circle"):
        engine.change_color("green")
        circle = Circle((1, 1), 7, engine)
        engine.add_figure(circle)
    with allure.step("Draw circle and verify updated output"):
        engine.draw()
        captured2 = prepare_output(capsys)
        check_count_output(captured2, 1)
        check_equal(captured2[0], expected2)


@allure.feature("Engine Integration")
@allure.story("Empty engine drawing")
def test_empty_engine_integration(capsys):
    with allure.step("Create engine without figures"):
        engine = Engine2D()
    with allure.step("Draw engine and capture output"):
        engine.draw()
        captured = prepare_output(capsys)
    with allure.step("Verify no output is produced"):
        check_count_output(captured, 0)
