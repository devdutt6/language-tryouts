use std::mem;
pub fn run() {
    let mut first:Vec<String> = vec![String::from("dev"),String::from("dutt"),String::from("chudasama"),String::from("harsh"),String::from("aasim")];
    // let second:[&str;4] = ["dev","dutt","chudasama","harsh"];
    println!("first{:?}", first);
    println!("first 0{}", first[0]);

    first[4] = String::from("jimish");
    first.push(String::from("aasim"));
    first.push(String::from("extra"));
    println!("changed first{:?}", first);
    first.pop();
    println!("changed first again {:?}", first);
    println!("changed first again {:?}", first);
    println!("length first{:?}", first.len());
    println!("memory first{}", mem::size_of_val(&first));
    // println!("memory first{}", mem::size_of_val(&second));

    let slice: &[String] = &first[0..2];
    println!("sliced{:?}", slice);

    for x in first.iter() {
        println!("Names {}", x);
    }

    for x in first.iter_mut() {
        x.push_str("one");
    }
    println!("changed first again and again {:?}", first);
}