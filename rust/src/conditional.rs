pub fn run() {
    let age:i8 = 21;
    let is_checkedid:bool = false;
    if age>=22 && is_checkedid {
        println!("Your age is {} so what would you like to drink",age);
    }
    else if age>=22{
        println!("Show me your id");
    }
    else if age<22 && is_checkedid {
        println!("You may leave sir.");
    }
    else {
        println!("Please You may leave");
    }
}