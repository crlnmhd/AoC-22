use std::io::{self, BufRead};

#[derive(Debug)]
enum Direction {
    Left,
    Right,
    Top,
    Bottom,
}

static DIRECTIONS: [Direction; 4] = [
    Direction::Left,
    Direction::Right,
    Direction::Top,
    Direction::Bottom,
];

#[derive(Clone, Copy, Debug)]
struct IndexPair {
    row: usize,
    column: usize,
}

fn main() {
    let grid = get_input();
    assert_eq!(grid[0].len(), grid.len(), "expexted equal height and width");
    println!("Part1 {}", part1(grid.clone()));
    println!("Part2 {}", part2(grid));
}

fn part1(grid: Vec<Vec<u8>>) -> usize {
    let grid_size = grid.len();
    let mut visible_inside: Vec<Vec<bool>> = vec![vec![false; grid_size]; grid_size];

    for i in 0..grid_size {
        for direction in DIRECTIONS.iter() {
            let mut tallest = 0;
            for j in 0..grid_size {
                let rotated_index =
                    get_grid_index_rotation(IndexPair { row: i, column: j }, &direction, grid_size);
                let current_tree = grid[rotated_index.row][rotated_index.column];
                if current_tree > tallest || j == 0 {
                    tallest = current_tree;
                    visible_inside[rotated_index.row][rotated_index.column] = true;
                }
            }
        }
    }

    let visible_tree_count: usize = visible_inside
        .iter()
        .map(|row| row.iter().filter(|&&tree_visible| tree_visible).count())
        .sum();
    visible_tree_count
}

fn part2(grid: Vec<Vec<u8>>) -> u64 {
    let mut greatest_scenic_score = 0;
    let grid_size = grid.len();
    for row in 0..grid_size {
        for column in 0..grid_size {
            let scenic_score = get_scenic_score(IndexPair { column, row }, &grid);
            greatest_scenic_score = std::cmp::max(greatest_scenic_score, scenic_score);
        }
    }
    greatest_scenic_score
}

fn get_scenic_score(position: IndexPair, grid: &Vec<Vec<u8>>) -> u64 {
    DIRECTIONS
        .iter()
        .map(|direction| visible_distance(grid, &position, direction))
        .reduce(|product, val| product * val)
        .unwrap()
}

fn visible_distance(grid: &Vec<Vec<u8>>, starting_point: &IndexPair, direction: &Direction) -> u64 {
    let tree_height = grid[starting_point.row][starting_point.column];
    let mut visible_distance = 0;
    let mut position: IndexPair = *starting_point;
    while let Some(next_pos) = step_in_direction(&position, direction, grid.len()) {
        visible_distance += 1;
        let current_tree_height = grid[next_pos.row][next_pos.column];
        if current_tree_height >= tree_height {
            break;
        }
        position = next_pos;
    }
    visible_distance
}

fn step_in_direction(
    starting_point: &IndexPair,
    direction: &Direction,
    grid_size: usize,
) -> Option<IndexPair> {
    let mut row: i64 = starting_point.row.try_into().unwrap();
    let mut column: i64 = starting_point.column.try_into().unwrap();
    match direction {
        Direction::Left => column -= 1,
        Direction::Right => column += 1,
        Direction::Top => row += 1,
        Direction::Bottom => row -= 1,
    }
    if row < 0 || column < 0 {
        return None;
    }
    let new_point = IndexPair {
        column: column.try_into().unwrap(),
        row: row.try_into().unwrap(),
    };
    if new_point.row < grid_size && new_point.column < grid_size {
        return Some(new_point);
    }
    None
}

fn get_grid_index_rotation(index: IndexPair, rotation: &Direction, grid_size: usize) -> IndexPair {
    match rotation {
        Direction::Left => IndexPair {
            row: index.row,
            column: index.column,
        },
        Direction::Right => IndexPair {
            row: index.row,
            column: grid_size - 1 - index.column,
        },
        Direction::Top => IndexPair {
            row: index.column,
            column: index.row,
        },
        Direction::Bottom => IndexPair {
            row: grid_size - 1 - index.column,
            column: index.row,
        },
    }
}

fn get_input() -> Vec<Vec<u8>> {
    let stdin = io::stdin();
    let radix = 10;
    stdin
        .lock()
        .lines()
        .flatten()
        .map(|line| {
            line.trim()
                .chars()
                .map(|c| u8::try_from(c.to_digit(radix).unwrap()).unwrap())
                .collect()
        })
        .collect()
}
