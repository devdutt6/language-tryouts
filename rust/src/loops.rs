pub fn run() {
    let mut count = 0;

    loop {
        count += 1 ;
        println!("{}",count);
        if count == 20 {
            break;
        }
    }

    while count < 100 {
        if count % 3 == 0 {
            if count % 7 == 0 {
                println!("{}", "FizzBuzz");
                count += 1;
                continue;
            }
            println!("{}", "Fizz");
        }
        else if count % 7 == 0 {
            if count % 3 == 0 {
                println!("{}", "FizzBuzz");
                count += 1;
                continue;
            }
            println!("{}", "Buzz");
        }
        else if count % 7 == 0 && count % 3 == 0 {
            println!("{}", "FizzBuzz");
        }
        else {
            println!("{}", count);
        }
        count += 1;
    }

    for x in 1..100 {
        println!("{}",x);
    }
}