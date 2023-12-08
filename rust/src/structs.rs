// Traditional struct
// struct Color {
//     red: u8,
//     green: u8,
//     blue: u8
// }

// tuple structs
// struct Color (u8,u8,u8);

// struct with functionality
struct Person {
    first_name: String,
    last_name: String
}

impl Person {
    // to construct Person
    fn new(first: &str,last: &str) -> Person{
        Person {
            first_name: first.to_string(),
            last_name: last.to_string()
        }
    }

    // get Fullname
    fn full_name(&self) -> String {
        format!("{} {}",self.first_name,self.last_name)
    }

    // set last name
    fn set_last_name(&mut self,last: &str) {
        self.last_name = last.to_string();
    }

    //try
    fn edit(&mut self, first: &str ,last: &str) {
        self.first_name = first.to_string();
        self.last_name = last.to_string();
    }

    //fullname to tuple
    fn to_tuple(self) -> (String,String) {
       (self.first_name,self.last_name)
    }
}

pub fn run() {
    // Traditional
    // let mut c = Color {
        //     red: 255,
        //     green: 0,
        //     blue: 0
        // };

        // println!("Color: {} {} {}",c.red,c.green,c.blue);
        // c.green = 255;

        // println!("Color: {} {} {}",c.red,c.green,c.blue);

    // Traditional
    // let mut c = Color ( 255, 0, 0);

    // println!("Color: {} {} {}",c.0,c.1,c.2);
    // c.1 = 255;

    // println!("Color: {} {} {}",c.0,c.1,c.2);

    let mut p1 = Person::new("Devdutt","Chudasama");
    println!("first Name: {}",p1.first_name);
    println!("first Name: {}",p1.last_name);
    println!("full Name: {}",p1.full_name());
    p1.set_last_name("Jadeja");
    println!("New full Name: {}",p1.full_name());
    p1.edit("Badrik","patel");
    println!("New full Name: {}",p1.full_name());
    println!("tuple full Name: {:?}",p1.to_tuple());
}