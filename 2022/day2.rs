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
        //println!("{}", line);
        vec.push(line);
    }
    
    let mut total: i32 = 0;
    for pair in vec {
        let split = pair.split(" ");
        let vp = split.collect::<Vec<&str>>();
        total += move_points(vp[1]);
        total += win_points(vp[0], vp[1]);
    }

    println!("{:?}", total);
    Ok(())
}

fn move_points(p0: &str) -> i32 {
    let rules = HashMap::from([
        ("X", 1), ("Y", 2), ("Z", 3),
        ]);
    //println!("{}", p0);
    rules[&p0]
}
fn win_points(p0: &str, p1: &str) -> i32 {
    let rules = HashMap::from([
             (("X","C"), 6), (("Y","A"), 6), (("Z","B"), 6), 
             (("X","A"), 3), (("Y","B"), 3), (("Z","C"), 3),
             (("X","B"), 0), (("Y","C"), 0), (("Z","A"), 0),
        ]);
    let key = (p1, p0);
    //println!("{:?}", key);
    rules[&key]
}
