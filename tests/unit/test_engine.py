import pytest
from checkers.figure_checker import validate_triangle_vertices
from checkers.test_checker import check_equal, check_count_output
from engine2d.engine import Engine2D
from engine2d.figures.base_figure import StubFigure
from helpers.output_helper import prepare_output
import allure


@allure.feature("Engine Unit Tests")
@allure.story("Change Engine Color")
def test_change_color():
    with allure.step("Create engine and verify initial color"):
        engine = Engine2D()
        check_equal(engine.current_color, "black")
    with allure.step("Change engine color and verify"):
        engine.change_color("blue")
        check_equal(engine.current_color, "blue")


@allure.feature("Engine Unit Tests")
@allure.story("Clear canvas after draw")
def test_engine_clear_after_render():
    with allure.step("Create engine and add stub figure"):
        engine = Engine2D()
        engine.add_figure(StubFigure())
        check_count_output(engine.canvas, 1)
    with allure.step("Draw engine and verify canvas is cleared"):
        engine.draw()
        check_count_output(engine.canvas, 0)


@allure.feature("Triangle Validation")
@allure.story("Valid triangle vertices")
def test_validate_triangle_vertices_success():
    with allure.step("Validate triangle vertices with valid tuples"):
        validate_triangle_vertices([(1, 3), (4, 2), (1, 5)])


@allure.feature("Triangle Validation")
@allure.story("Invalid triangle vertices")
def test_validate_triangle_vertices_failure():
    with allure.step("Validate triangle vertices with invalid input"):
        with pytest.raises(AssertionError):
            validate_triangle_vertices([1, 2])


@allure.feature("Engine Drawing")
@allure.story("Engine draw output")
def test_engine_draw(capsys):
    with allure.step("Create engine and add dummy figure"):
        engine = Engine2D(initial_color="orange")
        dummy = StubFigure()
        engine.add_figure(dummy)
    with allure.step("Draw engine"):
        engine.draw()
    with allure.step("Capture and verify output"):
        output = prepare_output(capsys)
        check_count_output(output, 1)
        check_equal(output[0], 'Done')
