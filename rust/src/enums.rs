enum Movement {
    Up,Down,Left,Right
}

fn _move (m: Movement) {
    match m {
        Movement::Up => println!("{}","Moved Up"),
        Movement::Down => println!("{}","Moved Down"),
        Movement::Left => println!("{}","Moved Left"),
        Movement::Right => println!("{}","Moved Right"),
    }
}

pub fn run() {
    let up = Movement::Up;
    let left = Movement::Left;
    let down = Movement::Down;
    let right = Movement::Right;

    _move(up);
    _move(left);
    _move(down);
    _move(right);
}