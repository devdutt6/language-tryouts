mod print;
mod types;
mod string1;
mod tuple;
mod arrays;
mod vectors;
mod conditional;
mod loops;
mod func;
mod pointer_ref;
mod structs;
mod enums;
mod cli;

fn main() {
    print::print();
    types::run();
    string1::run();
    tuple::run();
    arrays::run();
    vectors::run();
    conditional::run();
    loops::run();
    func::run();
    pointer_ref::run();
    structs::run();
    enums::run();
    cli::run();
}
