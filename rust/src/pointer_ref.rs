pub fn run() {
    // with primitives
    let arr1 = [1,2,3];
    let arr2 = arr1;
    println!("arr1: {:?} arr2: {:?}",arr1 ,arr2);

    // with nonprimitives, if you assign a variable to another then first varibale will no longer exists with the value
    // to achive the use refrence pointer
    let vec1 = vec![1,2,3];
    let vec2 = &vec1;
    println!("arr1: {:?} arr2: {:?}",&vec1 ,vec2);


}