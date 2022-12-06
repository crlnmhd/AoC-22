import sys


def main():
    seq = [line.strip() for line in sys.stdin]
    #print(f'{seq}')
    assert len(seq) == 1
    prob1_tests()
    print(f'Problem 1: {prob1(seq[0])}')
    prob2_tests()
    print(f'Problem 2 solution: {prob2(seq[0])}')


def prob1(line) -> int:
    for i in range(4, len(line)):
        prev = line[i - 4:i]
        if len(set(prev)) == 4:
            return i
    raise AssertionError('No starting point found')


def prob1_tests():
    assert prob1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert prob1('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert prob1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert prob1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11


def prob2(line: str) -> int:
    for i in range(14, len(line)):
        prev = line[i - 14:i]
        if len(set(prev)) == 14:
            return i
    raise AssertionError('No starting point found')


def prob2_tests():
    assert prob2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert prob2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert prob2('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert prob2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert prob2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26


if __name__ == "__main__":
    main()
