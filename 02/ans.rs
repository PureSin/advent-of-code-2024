#[path = "../util.rs"]
mod util;
use util::read_input;

fn main() {
    let lines = read_input("sample.txt");
    let (a, b) = solution(lines);
    println!("{0}, {1}", a, b);
}


fn solution(lines: Vec<String>) -> (i32, i32) {
    (0, 1)
}