use std::env;

pub fn run() {
    let args: Vec<String> = env::args().collect();
    let command = args[1].clone();

    if command == "Hello" {
        println!("This is how you make a cli application");
    }
    else if command == "Hi" || command == "hi" {
        println!("HI there");
    }
    else if command == "Namaste" || command == "namaste" {
        println!("Indian huh! welcome");
    }
    else if command == "aarigato" || command == "moshi_mosh" {
        println!("Japanese ora");
    }
    else {
        println!("Invalid Say greeting too");
    }
}