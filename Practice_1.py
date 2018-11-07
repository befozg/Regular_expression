def reg_exp_input():
    reg_exp = input().replace(' ', '')
    full_stdin = [list(reg_exp), input(), input()]
    return full_stdin


def kleene_star(last_set, pattern, k, prefixes_set):
    result_set = set()
    prefix = pattern * k
    for word in last_set:
        if word == '':
            pass
        else:
            if word in prefixes_set:
                result_set.add(prefix)
            elif word[0] == pattern:
                new_let = word
                for i in range(k):
                    result_set.add(new_let)
                    new_let += word
                result_set.add('')
            else:
                result_set.add('')
    return result_set


def not_pattern_letter(pattern):
    if pattern == 'a':
        return 'b'
    return 'a'


def concatenate(set_1, set_2):
    result_set = set()
    for first in set_1:
        for second in set_2:
            result_set.add(first + second)
    return result_set


def plus(set1, set2):
    result_set = set1 | set2
    return result_set


def check_for_prefix(word, prefix):
    if word[0:len(prefix)] == prefix:
        return True
    else:
        return False


def check_for_alphabet_existence(letter, alphabet):
    if letter not in alphabet:
        raise Exception


def check_for_length_of_pattern(in_power):
    if (not isinstance(in_power, int)) or (in_power <= 0):
        raise Exception


def does_the_prefix_exist(reg_exp, pattern, in_power):
    alphabet = {'a', 'b', 'c', '1', '.', '+', '*'}
    prefixes_set = get_prefixes_set(pattern, in_power)
    stack = []
    check_for_alphabet_existence(pattern, alphabet)
    check_for_length_of_pattern(in_power)
    not_pattern = not_pattern_letter(pattern)
    for letter in reg_exp:
        new_set = set(letter)
        check_for_alphabet_existence(letter, alphabet)
        if letter == "*":
            last_set = stack.pop()
            stack.append(kleene_star(last_set, pattern, in_power, prefixes_set))
        elif letter == '.':
            second = stack.pop()
            first = stack.pop()
            stack.append(concatenate(first, second))
        elif letter == '+':
            second = stack.pop()
            first = stack.pop()
            stack.append(plus(first, second))
        elif letter == pattern:
            stack.append(new_set)
        elif letter == '1':
            stack.append('')
        else:
            stack.append(set(not_pattern))

    prefix = pattern * in_power
    for word in stack[0]:
        if check_for_prefix(word, prefix):
            return "YES"
    return "NO"


def get_prefixes_set(x, k):
    prefixes_set = set()
    letter = ''
    for s in range(k):
        letter += x
        prefixes_set.add(letter)
    return prefixes_set


try:
    std_input = reg_exp_input()
    print(does_the_prefix_exist(std_input[0], std_input[1], int(std_input[2])))
except Exception:
    print("ERROR")
