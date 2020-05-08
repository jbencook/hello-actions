import math

import torch

from .hello import almost_pi


def test_almost_pi():
    assert abs(almost_pi() - math.pi) < 1e-11


def test_has_gpu():
    assert torch.cuda.is_available()
