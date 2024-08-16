/*
// Problem Statement: Find the largest string in an array of strings.


word -   hello i'm shubham full stack developer 


*/

//////////////////////////
const longestword = (str) => {
  if (str.trim().length === 0) {
    return false;
  }

  word = str.split(" ");
  word = word.sort((a, b) => b.length - a.length);
  console.log(word);

  return word[0];
};

console.log(longestword("hello welcome to my program and chek a longest word"));

// //////////////////////////////
let LongestWord = "hello welcome to my channel shubhmtech";

function x(s) {
  if (s.trim().length === 0) {
    return false;
  }

  word = s.split(" ");
  //   console.log(word);

  word = word.sort((a, b) => a.length - b.length);
  console.log(word);

  return word[0];
}

x(LongestWord);

/////////////////

const obj = "hello i'm shubhma welcome to word";

function obj1(x) {
  // console.log(x);

  if (x.trim().length === 0) {
    return false;
  }

  word = x.split(" ");
  word = word.sort((a, b) => a.length - b.length);
  //    word.at(-1);

  /// print a last word used   at(-1)
  console.log(word.at(-1));
}

obj1(obj);

// core way to find

// console.log(String);

// function LargString(z) {
//   if (z.length === 0) {
//     return false;
//   }
//   let y = z[0];

//   for (let i = 1; i < z.length; i++) {
//     if
//   }

// }

// const String =
//   "This code defines a function to find and return the largest string in an array.";
// console.log(LargString(String));

// Problem Statement: Find the largest string in an array of strings.

function findLargestString(strings) {
  if (strings.length === 0) return null;

  let largestString = strings[0];

  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > largestString.length) {
      largestString = strings[i];
    }
  }

  return largestString;
}

// Example usage:
const stringArray = ["apple", "banana", "cherry", "date"];
console.log(findLargestString(stringArray)); // Output: "banana"

// write own

function LongString(str) {
  // console.log(str);

  if (str.length === 0) {
    return false;
  }

  word = str.split(" ");
  //   console.log(word);

  let largestNum = word[0];

  for (let i = 0; i < word.length; i++) {
    if (word.split) {
      return " ";
    }
    if (word.length > largestNum.length) {
      largestNum = word[i];
    }
    console.log(largestNum);
  }
  // return console.log(largestNum);
}

const String1 =
  "This code defines a function to find and return the largest string in an array.";

LongString(String1);
