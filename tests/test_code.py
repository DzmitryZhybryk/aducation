from contextlib import nullcontext as does_not_raise

import pytest

from tests.my_code import Calculator

class TestCalculator:

    @pytest.mark.parametrize(
            "x, y, res, expectation",
            [
                (1, 2, 0.5, does_not_raise()),
                (5, -1, -5, does_not_raise()),
                (1, "2", 7, pytest.raises(TypeError)),
            ]
    )
    def test_devide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res



    @pytest.mark.parametrize(
            "x, y, res",
            [
                (1, 2, 3),
                (5, -1, 4)
            ]
    )
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res