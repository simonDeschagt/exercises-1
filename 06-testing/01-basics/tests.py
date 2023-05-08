from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((0,3), (3,5))
    assert overlapping_intervals((0,3), (1,2))
    assert overlapping_intervals((1,3), (0,1))

def test_niet_overlappend():
    assert not overlapping_intervals((2,5), (7,10))
    assert not overlapping_intervals((0,2), (3,5))
    assert not overlapping_intervals((2,3), (0,1))

def test_verkeerde_waarden():
    assert not overlapping_intervals((4,1), (2,4))