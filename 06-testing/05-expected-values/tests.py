import pytest
from mergesort import split_in_two, merge_sorted, merge_sort
import itertools

@pytest.mark.parametrize('ns',[
    list(range(k)) for k in range(101)
])
def test_split_in_two(ns):
    left, right =  split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1


@pytest.mark.parametrize('left', [
    [],
    [1],
    [1,2,8,9],
    [1,2,3,3,4,5],
    [1,2,3,4,5,6]
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [1,2,8,9],
    [1,2,3,3,4,5],
    [1,2,3,4,5,6]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)


@pytest.mark.parametrize('expected, ns', [
    (ns, list(permutation))
    for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected
