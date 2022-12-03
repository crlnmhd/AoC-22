import sys


def prob1(seq):
    total = 0
    for line in seq:
        comp1, comp2 = split_compartments(line)
        common = set(comp1) & set(comp2)
        assert len(common) == 1
        total += value(list(common)[0])
    return total


def prob2(seq):
    total = 0
    for i in range(0, len(seq), 3):
        e1, e2, e3 = seq[i], seq[i + 1], seq[i + 2]
        common = set(e1) & set(e2) & set(e3)
        assert len(common) == 1
        total += value(list(common)[0])
    return total


def split_compartments(seq) -> tuple[list, list]:
    half_point = len(seq) // 2
    comp1, comp2 = seq[0:half_point], seq[half_point:]
    assert len(comp1) == len(comp2)
    assert len(seq) == len(comp1) + len(comp2)
    return comp1, comp2


def value(letter: str) -> int:
    letter_value = ord(letter)
    if ord('a') <= letter_value <= ord('z'):
        return letter_value - ord('a') + 1
    elif ord('A') <= letter_value <= ord('Z'):
        return letter_value - ord('A') + 27
    raise RuntimeError('messed up')


if __name__ == '__main__':
    seq = [line.strip() for line in sys.stdin]
    print(prob1(seq))
    print(prob2(seq))
