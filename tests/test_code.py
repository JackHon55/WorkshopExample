import numpy as np
import pytest

from some_module import integrate_trapz


# Testing the zero case. Plenty of other tests to write!
def test_integrate_trapz_1():
    xs, ys = np.linspace(0, 10, 10), np.zeros(10)
    assert integrate_trapz(xs, ys) == 0

# Test a point function
def test_integrate_point():
    xs, ys = np.zeros(10) + 1, np.linspace(0,10,10)
    assert integrate_trapz(xs, ys) == 0

def test_integrate_string():
    xs, ys = np.asarray(['Hello','how','are','you']),np.linspace(0,10,10)
    assert integrate_trapz(xs,ys) == 10

# Testing too much - ensuring it fails on weird input
# Normally this would be an AssertionException or a specific
# exception, not the general Exception class.
def test_integrate_trapz_failure():
    with pytest.raises(Exception):
        integrate_trapz("Some", "Values")
