pub fn run() {
    let a = "Devdutt";
    // 'a' is immutable string this is string type it cant be changed
    println!("Devdutt {}",a);
    // println!("{}",a.capacity());
    // this function is only used for string types not this
    let mut b = "Badrik";
    println!("Badrik {}",b);
    b = "Patel";
    println!("Patel {}",b);
    // println!("{}",b.capacity());
    // this function is only used for string types not to mutabel string


    let mut string2 = String::from("Hello ");
    let string3 = String::with_capacity(32);
    println!("Hello {}",string2);
    string2.push('W');
    string2.push_str("orld!");
    println!("Hello World{}",string2);
    println!("String2 capacity{}",string2.capacity());
    println!("String3 capacity{}",string3.capacity());
    println!("String2 length{}",string2.len());
    println!("String3 capacity{}",string3.len());
    println!("String2 isEmpty{}",string2.is_empty());
    println!("String2 Contains{}",string2.contains("World"));
    println!("String2 replace{}",string2.replace("World", "there"));
    println!("String2 replace{}",string2.replace("world", "there"));

    for word in string2.split_whitespace() {
        println!("{}",word);
    }

    assert_eq!(string3.capacity(),32);






}