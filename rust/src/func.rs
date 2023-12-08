pub fn run() {
    greet("Hello", "Devdutt");
    let sum = add(12,14);
    println!("Sum: {}",sum);
    // closures
    let n3: i32 = 10;
    let add_ten = |n1: i32, n2: i32| n1+ n2+ n3;
    let adding_ten = add_ten(12,14);
    println!("ten: {}",adding_ten);
}
// Parameter function
fn greet(greet: &str ,name: &str) {
    println!("Greetings: {} {}",greet,name);
}
// returning function
fn add(n1: i32, n2: i32) -> i32 {
    n1 + n2
}
