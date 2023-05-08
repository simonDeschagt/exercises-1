import pytest 
from statistics import average


@pytest.mark.parametrize('ns, expected',[
    ([1,2,3,4,5], 3),
    ([2,4,6,8], 5),
    ([], 0),
    ([10,-1,2], 11/3),
    ([0,0,0,0], 0),
    ([-1,-2,-3,3], -3/4),
    ([0.1,0.1,0.1], 0.1),
])
def test_average(ns, expected):
    a = average(ns)
    assert pytest.approx(expected, abs=0.1) == a