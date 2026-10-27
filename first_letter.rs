use std::time::Instant;

struct Solution;

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut seen: u32 = 0;

        for c in s.chars() {
            let bit = 1 << (c as u8 - b'a');
            if seen & bit != 0 {
                return c;
            }
            seen |= bit;
        }

        // Optional: fallback return for valid inputs (shouldn't happen)
        panic!("No character appears twice");
    }
}

fn time_repeated_character() {
    let s = "abcdefgahijklmno".to_string();
    let start = Instant::now();
    let _ = Solution::repeated_character(s);
    let duration = start.elapsed();
    println!("Duration as Nanoseconds: {} ns", duration.as_nanos());
}

fn main() {
    time_repeated_character();
}

