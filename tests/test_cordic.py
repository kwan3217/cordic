"""
Test and exercise the CORDIC algorithm

Created: 5/31/24
"""
import itertools
from typing import Callable

import numpy as np
import pytest

from cordic import sin_taylor1, fac, sin_taylor2, sin_taylor3


@pytest.mark.parametrize(
    "n,ref_fac",[
        (0,  1),
        (1,  1),
        (2,  2),
        (3,  6),
        (4, 24),
        (5,120),
        (6,720)
    ]
)
def test_fac(n:int,ref_fac:int):
    assert fac(n)==ref_fac


@pytest.mark.parametrize(
    "theta,refsin,f",[(theta,np.sin(theta),f) for theta,f in itertools.product(
        (0.0,0.5,1.0),
         (np.sin,sin_taylor1,sin_taylor2,sin_taylor3))]
)
def test_sin(theta:float,refsin:float,f:Callable[[float],float]):
    print(f"\n{f(theta):17.15f},{refsin:17.15f},{f(theta)-refsin:18.15f}")
    assert np.isclose(f(theta),refsin)