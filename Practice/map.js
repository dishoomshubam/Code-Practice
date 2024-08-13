const user = [
  {
    name: "shubham",
    lastname: "kharche",
  },
];

function data(x) {
  return x.name;
}

const arr = [2, 3, 2, 3, 3];

function x(y) {
  return y * 2;
}

const output = user.map(data);

console.log(output);

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

const arr = [1, 2, 3, 4, 5];

function x(arr) {
  return arr * 2;
}

let y = arr.map(x);

console.log(y);
