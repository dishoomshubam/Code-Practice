const obj1 = [
    {
      name: "shubham",
      lastname: "kharche",
      age: "58",
    },
    {
      name: "chirag",
      lastname: "patil",
      age: "34",
    },
  ];
  
  function x(arr) {
    if (arr < 50) {
      arr.age;
    }
  
    return arr;
  }
  
  const obj2 = obj1.map(x);
  
  console.log(obj2);
  