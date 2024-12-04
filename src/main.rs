use regex::Regex;

#[path = "../util.rs"]
mod util;
use util::read_input;

fn main() {
    let lines = read_input("input.txt");
    let (a, b) = solution(lines);
    println!("{0}, {1}", a, b);
}


fn solution(lines: Vec<String>) -> (i32, i32) {
    let mut part1_total = 0;
    let mut part2_total = 0;

    let combined_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)";
    let combined_input = lines.join("");
    let matches: Vec<_> = Regex::new(combined_pattern)
        .unwrap()
        .find_iter(&combined_input)
        .collect();

    let mut can_mut = true;
    for m in matches {
        let match_str = m.as_str();
        if match_str.starts_with("mul") {
            // Extract numbers using regex
            let nums: Vec<_> = Regex::new(r"\d+")
                .unwrap()
                .find_iter(match_str)
                .map(|m| m.as_str().parse::<i32>().unwrap())
                .collect();
            
            let x = nums[0];
            let y = nums[1];
            
            part1_total += x * y;
            if can_mut {
                part2_total += x * y;
            }
        } else if match_str.starts_with("don't") {
            can_mut = false;
        } else if match_str.starts_with("do") {
            can_mut = true;
        }
    }
    (part1_total, part2_total)
}