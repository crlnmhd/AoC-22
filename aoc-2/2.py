import sys
from dataclasses import dataclass


scores = {'loss': 0, 'draw': 3, 'win': 6}
winning_moves = {'A': 'Y', 'B': 'Z', 'C': 'X'}
choise_scores = {'X': 1, 'Y': 2, 'Z': 3}
same = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}


def prob1(moves):
    return sum(score(opponent=move[0], my=move[1]) for move in moves)


def prob2(moves):
    outcomes = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}
    score = 0
    for opponent, outcome in moves:
        outcome = outcomes[outcome]
        if outcome == 'loss':
            score += scores[outcome] + choise_scores[loss[opponent]]
        elif outcome == 'draw':
            score += scores[outcome] + choise_scores[same[opponent]]
        else:
            score += scores[outcome] + choise_scores[winning_moves[opponent]]
    return score


def score(opponent: str, my: str):
    if my == same[opponent]:
        return scores['draw'] + choise_scores[my]
    elif my == winning_moves[opponent]:
        return scores['win'] + choise_scores[my]
    else:
        return scores['loss'] + choise_scores[my]


if __name__ == '__main__':
    seq = [line.strip() for line in sys.stdin]
    moves = [line.split() for line in seq]
    print(moves)
    print(prob1(moves))
    print(prob2(moves))
