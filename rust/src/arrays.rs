use std::mem;

pub fn run() {
    let mut first:[&str;5] = ["dev","dutt","chudasama","harsh","aasim"];
    let second:[&str;4] = ["dev","dutt","chudasama","harsh"];
    println!("first{:?}", first);
    println!("first 0{}", first[0]);

    first[4] = "jimish";
    println!("changed first{:?}", first);
    println!("length first{:?}", first.len());
    println!("memory first{}", mem::size_of_val(&first));
    println!("memory first{}", mem::size_of_val(&second));

    let slice: &[&str] = &first[0..2];
    println!("sliced{:?}", slice);


}