from .context import ap
import pytest

@pytest.fixture
def airplane():
    """Creates an Airplane instance with position(0,0), initial fuel of 10 litres and a consumption of 2 litres/km"""
    return ap.Airplane(0, 0, 2, 10)


def test_refuel(airplane):
    airplane.refuel(10)
    assert airplane.fuel_level == 20


def test_refuel_raises_exception_on_negative_fuel(airplane):
    with pytest.raises(ap.NegativeLitres):
        airplane.refuel(-10)


def test_refuel_raises_exception_on_bad_fuel(airplane):
    with pytest.raises(TypeError):
        airplane.refuel('a')


def test_goto_not_enough_fuel(airplane):
    assert airplane.goto(7,7) == False


@pytest.mark.parametrize("refuel,fuel_level,position_x,position_y,fuel_after_moving", [
    (200, 210, 7, 7, 210-2*98),
])
def test_goto_fuel(airplane,refuel,fuel_level,position_x,position_y,fuel_after_moving):
    airplane.refuel(refuel)
    assert airplane.fuel_level == fuel_level
    assert airplane.goto(position_x,position_y) == True
    assert airplane.position == (position_x,position_y)
    assert airplane.fuel_level == fuel_after_moving
