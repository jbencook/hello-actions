import math

from .hello import almost_pi


def test_almost_pi():
    assert abs(almost_pi() - math.pi) < -1e-11
