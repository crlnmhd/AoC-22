import sys


def main():
    lines = [line.strip() for line in sys.stdin]
    assert len(lines) == 1
    line = lines[0]
    prob1_tests()
    print(f'Problem 1: answer {index_of_unique_sequence(line,4)}')
    prob2_tests()
    print(f'Problem 2 answer: {index_of_unique_sequence(line,14)}')


def index_of_unique_sequence(line: str, n: int) -> int:
    for i in range(n, len(line)):
        prev = line[i - n:i]
        if len(set(prev)) == n:
            return i
    raise AssertionError('No starting point found')


def prob1_tests():
    assert index_of_unique_sequence(
        'bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
    assert index_of_unique_sequence(
        'nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
    assert index_of_unique_sequence(
        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
    assert index_of_unique_sequence(
        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11


def prob2_tests():
    assert index_of_unique_sequence(
        'mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    assert index_of_unique_sequence(
        'bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    assert index_of_unique_sequence(
        'nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    assert index_of_unique_sequence(
        'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    assert index_of_unique_sequence(
        'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26


if __name__ == "__main__":
    main()
