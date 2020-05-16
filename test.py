from Practice_1 import does_the_prefix_exist


def test_for_yes_1():
    assert (does_the_prefix_exist("a**aa..", "a", 8) == "YES")


def test_for_yes_2():
    assert (does_the_prefix_exist("a1.b+c+a.bc++*", "b", 2) == "YES")


def test_for_yes_3():
    assert (does_the_prefix_exist("ab+c+a.bc++*", "c", 6) == "YES")


def test_try_except_letter_error():
    try:
        does_the_prefix_exist("ab+c+ccc...d2.*", "a", 5)
    except Exception:
        return ("ERROR")


def test_try_except_k_error():
    try:
        does_the_prefix_exist("ab+c+ccc...a*", "a", -1)
    except Exception:
        return ("ERROR")


def test_try_except_x_error():
    try:
        does_the_prefix_exist("ab+c+ccc..1..a*", "z", 2)
    except Exception:
        return ("ERROR")


def test_try_except_stack_error():
    try:
        does_the_prefix_exist("ab+c+ccc...*.", "a", 2)
    except Exception:
        return ("ERROR")


def test_for_error_1():
    assert (test_try_except_letter_error() == "ERROR")


def test_for_error_2():
    assert (test_try_except_k_error() == "ERROR")


def test_for_error_3():
    assert (test_try_except_x_error() == "ERROR")


def test_for_error_3():
    assert (test_try_except_stack_error() == "ERROR")


def test_for_no_1():
    assert (does_the_prefix_exist("1*a.c*.", "c", 3) == "NO")


def test_for_no_2():
    assert (does_the_prefix_exist("acb..ab+.*ab+.ac.a*.", "c", 3) == "NO")


def test_for_no_3():
    assert (does_the_prefix_exist("ab.c.a.a.a.a.*", "a", 4) == "NO")


#test_for_yes_1()
#test_for_yes_2()
#test_for_yes_3()
#test_for_no_1()
#test_for_no_2()
#test_for_no_3()
#test_try_except_x_error()
#test_try_except_k_error()
#test_try_except_letter_error()
#test_try_except_stack_error()
