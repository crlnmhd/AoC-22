use std::{
    collections::HashMap,
    io::{self, BufRead},
};

fn main() {
    let input = get_input();
    let mut path: Vec<String> = Vec::new();
    let mut dir_sizes: HashMap<String, u64> = HashMap::new();

    for line in input.iter() {
        if line == "$ cd .." {
            path.pop();
            continue;
        }
        if let Some(destination) = remaining_after(&line, "$ cd ") {
            path.push(destination.to_string());
            continue;
        }
        if line == "$ ls" || line.starts_with("dir") {
            continue;
        }

        let size: Vec<&str> = line.split(" ").take(1).collect();
        let size = size[0].parse::<u64>().expect("Could not parse integer!");

        // Add size to directory and parent directories.
        for level in 0..path.len() {
            let dir_path = path.as_slice()[..level + 1].join("/");
            let size_of_dir = dir_sizes.entry(dir_path);
            *size_of_dir.or_default() += size;
        }
    }
    let part1_solution: u64 = dir_sizes
        .clone()
        .into_values()
        .filter(|&v| v < 100_000)
        .sum();

    let fs_size = dir_sizes.get("/").unwrap();
    let required_space = fs_size - (70_000_000 - 30_000_000);
    let part2_solution = dir_sizes
        .into_values()
        .filter(|&dir_size| dir_size >= required_space)
        .min()
        .unwrap();

    println!("Part1: {}", part1_solution);
    println!("Part2: {}", part2_solution);
}

fn remaining_after<'a>(whole: &'a str, begining: &'a str) -> Option<&'a str> {
    if let Some(_) = whole.find(begining) {
        return Some(&whole[begining.len()..]);
    }
    None
}

fn get_input() -> Vec<String> {
    let stdin = io::stdin();
    let input: Vec<String> = stdin.lock().lines().flatten().collect();
    let input = input.iter().map(|line| line.trim().to_string()).collect();
    return input;
}
