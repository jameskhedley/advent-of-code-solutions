use std::collections::HashMap;
use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    //let f = File::open("day2_ex.txt")?;
    let f = File::open("day2.txt")?;
    let f = BufReader::new(f);
    
    let mut vec = Vec::new();

    for line in f.lines() {
        let line = line.unwrap();
        vec.push(line);
    }
    
    let mut total: i32 = 0;
    for pair in vec {
        let split = pair.split(" ");
        let vp = split.collect::<Vec<&str>>();
        total += move_points(vp[0], vp[1]);
        total += win_points(vp[1]);
    }

    println!("{:?}", total);
    Ok(())
}

fn move_points(p0: &str, p1: &str) -> i32 {
    let rules = HashMap::from([
             (("X","C"), "Y"), (("Y","A"), "X"), (("Z","B"), "Z"), 
             (("X","A"), "Z"), (("Y","B"), "Y"), (("Z","C"), "X"),
             (("X","B"), "X"), (("Y","C"), "Z"), (("Z","A"), "Y"),
        ]);
        
    let key = (p1, p0);
    let points = HashMap::from([
        ("X", 1), ("Y", 2), ("Z", 3),
        ]);
    //println!("{}", p0);
    points[rules[&key]]
}
fn win_points(p0: &str) -> i32 {
    let rules = HashMap::from([
        ("X", 0), ("Y", 3), ("Z", 6),
        ]);
    rules[&p0]
}
