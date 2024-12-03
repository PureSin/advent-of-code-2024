fn main() {
    let lines = read_input();
    println!("{}", solution(lines))
}

fn parse_to_lists(lines: &Vec<String>) -> (Vec<i32>, Vec<i32>) {
    let mut list1 = Vec::new();
    let mut list2 = Vec::new();
    
    for line in lines {
        let nums: Vec<i32> = line.split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        list1.push(nums[0]);
        list2.push(nums[1]);
    }
    
    (list1, list2)
}

fn solution(lines: Vec<String>) -> i32 {
    let (mut list1, mut list2) = parse_to_lists(&lines);
    list1.sort();
    list2.sort();
    let mut sum = 0;
    for i in 0..list1.len() {
        sum += (list1[i] - list2[i]).abs();
    }
    sum
}

fn read_input() -> Vec<String> {
    // Read input filr
    let input = std::fs::read_to_string("input.txt")
        .expect("Failed to read input file");
    
    // Split into lines
    input.lines()
        .map(String::from)
        .collect()
}