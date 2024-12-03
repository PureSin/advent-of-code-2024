pub fn read_input(filename: &str) -> Vec<String> {
    // Read input file
    let input = std::fs::read_to_string(filename)
        .expect("Failed to read input file");
    
    // Split into lines
    input.lines()
        .map(String::from)
        .collect()
} 