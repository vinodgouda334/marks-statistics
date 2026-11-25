import pytest
from marks_statistics import (
    validate_marks,
    total_marks,
    average_marks,
    highest_marks,
    lowest_marks,
)


def test_validate_marks():
    assert validate_marks([50, 60]) == [50, 60]


def test_invalid_marks():
    with pytest.raises(ValueError):
        validate_marks([110, 50])


def test_total_marks():
    assert total_marks([78, 85, 92, 66, 89]) == 410


def test_average_marks():
    assert average_marks([80, 90, 100]) == pytest.approx(90.0)


def test_highest_marks():
    assert highest_marks([78, 85, 92, 66, 89]) == 92


def test_lowest_marks():
    assert lowest_marks([78, 85, 92, 66, 89]) == 66
