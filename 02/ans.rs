#[path = "../util.rs"]
mod util;
use util::read_input;

fn main() {
    let lines = read_input("input.txt");
    let (a, b) = solution(lines);
    println!("{0}, {1}", a, b);
}

fn is_valid_2(levels: &Vec<i32>) -> bool {
    if is_valid(levels) {
        return true;
    }

    // Try removing each element and check if the remaining sequence is valid
    if (0..levels.len()).any(|i| {
        let mut modified = levels.clone();
        modified.remove(i);
        is_valid(&modified)
    }) {
        return true
    }
    false
}

fn is_valid(levels: &Vec<i32>) -> bool {
    // Check if list is monotonically increasing
    let increasing = levels.windows(2).all(|w| w[1] >= w[0]);
    // Check if list is monotonically decreasing
    let decreasing = levels.windows(2).all(|w| w[1] <= w[0]);
    
    // Return true if either increasing or decreasing
    let is_monotonic = increasing || decreasing;
    if !is_monotonic {
        return false;
    }

    // Check differences between consecutive numbers
    for w in levels.windows(2) {
        let diff = (w[1] - w[0]).abs();
        if diff < 1 || diff > 3 {
            return false;
        }
    }
    true
}

fn solution(lines: Vec<String>) -> (i32, i32) {
    let levels = lines.iter()
        .map(|line| line.split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>())
        .collect::<Vec<Vec<i32>>>();
    let part1_score = levels.iter()
        .filter(|nums| is_valid(nums))
        .count() as i32;
    let part2_score = levels.iter()
        .filter(|nums| is_valid_2(nums))
        .count() as i32;
    (part1_score, part2_score)
}