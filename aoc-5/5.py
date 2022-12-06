import sys
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Step:
    number: int
    source: int
    destination: int


def main():
    seq = [line.strip("\n") for line in sys.stdin]
    print(seq)
    print(prob1(seq))
    print(prob2(seq))


def parse_input(lines: list[str]):
    separator_line = lines.index('')
    container_def = lines[:separator_line - 1]
    container_slots = lines[separator_line - 1]
    step_defs = lines[separator_line + 1:]

    number_of_slots = get_number_of_slots(container_slots)
    containers = [parse_container_description_line(
        line, number_of_piles=number_of_slots) for line in container_def]

    stacks = merge_containers(containers)
    steps = [parse_step(line) for line in step_defs]
    return stacks, steps


def get_number_of_slots(slot_description_line: str):
    return int(slot_description_line[-1])


def merge_containers(containers):
    number_of_stacks = len(containers[0])
    stacks = [[] for _ in range(number_of_stacks)]
    for line_ind in range(len(containers)):
        for stack_ind in range(number_of_stacks):
            if non_empty_container := containers[line_ind][stack_ind]:
                stacks[stack_ind] += non_empty_container

    print('merges stacks:', stacks)
    return stacks


def parse_step(step_line: str) -> Step:
    numbers = [int(x) for x in re.findall(r'\d+', step_line)]
    return Step(number=numbers[0], source=numbers[1], destination=numbers[2])


def parse_container_description_line(line: str, number_of_piles: int):
    piles = [[] for _ in range(number_of_piles)]
    characters = len(line)
    print(f"line with {len(line)} characters: '{line}'")
    characters = [line[i] for i in range(1, len(line), 4)]
    print("characters:", characters)
    for ind, character in enumerate(characters):
        if character.strip():
            piles[ind] += [character]
    return piles


def prob1(seq):
    containers, steps = parse_input(seq)
    print('containers:', containers)
    for step in steps:
        for _ in range(step.number):
            moved_container = containers[step.source - 1].pop(0)
            containers[step.destination - 1].insert(0, moved_container)
    top_of_stacks = [stack[0] for stack in containers]
    print('top stacks:', top_of_stacks)
    return ''.join(top_of_stacks)


def prob2(seq):
    containers, steps = parse_input(seq)
    print('containers:', containers)
    for step in steps:
        for i in range(step.number):
            moved_container = containers[step.source - 1].pop(0)
            containers[step.destination -
                       1].insert(i, moved_container)
    top_of_stacks = [stack[0] for stack in containers]
    print('top stacks:', top_of_stacks)
    return ''.join(top_of_stacks)


if __name__ == "__main__":
    main()
