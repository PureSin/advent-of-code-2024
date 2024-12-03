fn main() {
    let lines = read_input();
    let (a, b) = solution(lines);
    println!("{0}, {1}", a, b);
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

fn solution(lines: Vec<String>) -> (i32, i32) {
    let (mut list1, mut list2) = parse_to_lists(&lines);
    list1.sort();
    list2.sort();
    let part1_score = list1.iter()
        .zip(list2.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();

    // solve part 2 by turing list2 into a map 
    let mut list2_counts = std::collections::HashMap::new();
    for &num in list2.iter() {
        *list2_counts.entry(num).or_insert(0) += 1;
    }
    let mut score = 0;
    for &num in list1.iter() {
        score += list2_counts.get(&num).unwrap_or(&0) * num;
    }
    return (part1_score, score)
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