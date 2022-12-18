use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let lines: Vec<String> = stdin.lock().lines().flatten().collect();
    let instructions: Vec<&str> = lines.iter().map(|line| line.trim()).collect();

    let x_during_cycle = get_x_at_cycle(&instructions);
    println!("Part 1: {}", part1(&x_during_cycle));
    part2(&x_during_cycle);
}

fn part1(x_at_cycle: &Vec<i64>) -> i64 {
    let mut signal_strength = 0i64;
    for &cycle in [20, 60, 100, 140, 180, 220].iter() {
        println!(
            "At cycle {} we have value: {}",
            cycle,
            x_at_cycle[cycle - 1]
        );
        signal_strength += cycle as i64 * x_at_cycle[cycle - 1];
    }
    signal_strength
}

fn part2(x_at_cycle: &Vec<i64>) {
    for (cycle, &value) in x_at_cycle.iter().enumerate() {
        let horizontal_pos = cycle % 40;
        if horizontal_pos == 0 {
            println!("");
        }
        if (value - (horizontal_pos as i64)).abs() <= 1 {
            print!("#");
        } else {
            print!(".");
        }
    }
}

fn get_x_at_cycle(instructions: &Vec<&str>) -> Vec<i64> {
    let mut x = 1i64;
    let mut x_at_cycle: Vec<i64> = Vec::new();

    for &instruction in instructions.iter() {
        if instruction == "noop" {
            x_at_cycle.push(x);
        } else {
            let parameter: i64 = instruction
                .split(" ")
                .nth(1)
                .unwrap()
                .parse::<i64>()
                .unwrap();
            x_at_cycle.push(x);
            x_at_cycle.push(x);
            x += parameter;
        }
    }
    x_at_cycle
}
