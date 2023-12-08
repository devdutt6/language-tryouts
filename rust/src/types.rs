pub fn run() {
    let a = "Devdutt";
    let mut b = "Badrik";
    println!("{}",b);
    b = "Patel";
    let c : bool = true;
    let d : char = 'a';
    println!("max length for i32 {}",std::i32::MAX);
    println!("max length for i16 {}",std::i16::MAX);
    println!("max length for i64 {}",std::i64::MAX);
    println!("max length for i128 {}",std::i128::MAX);
    let exp : i32= 10+10;

    println!("{:?}",(a, b, c ,d,exp,'\u{1F600}'));

}