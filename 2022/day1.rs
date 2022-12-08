use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("day1.txt")?;
    let f = BufReader::new(f);
    
    let mut vec = Vec::new();

    for line in f.lines() {
        let line = line.unwrap();
        //println!("{}", line);
        if line != "" {
            let my_int = line.parse::<i32>().unwrap();
            vec.push(my_int);
        } else {
            vec.push(0);
        }
    }

    let mut pointer: usize = 0;
    let mut idx: usize = 0;
    let mut big: i32 = 0;
    
    for num in &vec {
        if *num==0 {
            let slice = &vec[pointer..idx];
            let sum: i32 = slice.iter().sum();
            if sum > big {
                big = sum;
            }
            pointer = idx+1;
        }
        idx += 1;
    }
    println!("{:?}", big);
    Ok(())
}
