import pytest
from Practice_1 import does_the_prefix_exist


def test_for_yes_1():
    assert (does_the_prefix_exist("a**aa..", "a", 8) == "YES")


def test_for_yes_2():
    assert (does_the_prefix_exist("a1.b+c+a.bc++*", "b", 2) == "YES")