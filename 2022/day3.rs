use std::collections::HashSet;
use std::iter::FromIterator;
use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    //let f = File::open("day3_ex.txt")?;
    let f = File::open("day3.txt")?;
    let f = BufReader::new(f);
       
    let mut vec = Vec::new();

    for line in f.lines() {
        let line = line.unwrap();
        vec.push(line);
    }
    
    let mut total: i32 = 0;
    for bp in vec {
        total += calc(&detect(&bp));
    }

    println!("{:?}", total);
    Ok(())
}

fn detect(s0: &str) -> char {
    let char_vec: Vec<char> = s0.chars().collect();
    println!("{:?}", char_vec);
    let cvl = &char_vec[0..char_vec.len()/2];
    let cvr = &char_vec[char_vec.len()/2..];
    println!("{:?}", cvl);
    println!("{:?}", cvr);
    
    let set_l: HashSet<&char> = HashSet::from_iter(cvl);
    let set_r: HashSet<&char> = HashSet::from_iter(cvr);
    println!("{:?}", set_l);
    println!("{:?}", set_r);
    let inters: _ = set_l.intersection(&set_r);
    let res: Vec<&&char> = inters.into_iter().collect();
    println!("{:?}", **res[0]);
    println!("{:?}", "===============================");
    **res[0]
}  

fn calc(c0: &char) -> i32 {
    let s0 = c0.to_string();
    let AB = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let res = AB.find(&s0).unwrap() as i32;
    //println!("{:?}", res);
    res+1
}
