import sys


def main(elfs):
    return max(sum(elf) for elf in elfs)


def prob2(elfs):
    elf_total = sorted([sum(elf) for elf in elfs], reverse=True)
    return sum(elf_total[:3])


if __name__ == '__main__':
    elf_carries = []
    elf = []
    for line in sys.stdin:
        if line.strip():
            elf += [int(line)]
        else:
            elf_carries += [elf]
            elf = []
    if elf:
        elf_carries += [elf]

    print('problem 1:', main(elf_carries))
    print('problem 2:', prob2(elf_carries))
