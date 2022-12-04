import sys


def main():
    seq = [line.strip().split(',') for line in sys.stdin]
    seq = [[elf.split('-') for elf in line] for line in seq]
    seq = [[[int(x) for x in elf] for elf in line] for line in seq]
    print(prob1(seq))
    print(prob2(seq))


def prob1(seq):
    covers = 0
    for line in seq:
        e1, e2 = [set(range(e[0], e[1] + 1)) for e in line]
        if e1 <= e2 or e2 <= e1:
            covers += 1
    return covers


def prob2(seq):
    pairs_with_overlap = 0
    for line in seq:
        e1, e2 = [set(range(e[0], e[1] + 1)) for e in line]
        if e1 & e2:
            pairs_with_overlap += 1
    return pairs_with_overlap


if __name__ == '__main__':
    main()
