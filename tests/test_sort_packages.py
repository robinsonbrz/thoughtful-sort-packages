import pytest
from src.sort_packages import sort_packages

def test_sort_packages_rejected():
    result = sort_packages(100,100,101,21)
    assert result == 'REJECTED'

def test_sort_packages_standard():
    result = sort_packages(100,100,99,19)
    assert result == 'STANDARD'

def test_sort_packages_():
    result = sort_packages(100,100,101,19)
    assert result == 'SPECIAL'

    result = sort_packages(100,100,99,21)
    assert result == 'SPECIAL'
