/** @format */

let number = 1;

function Chekc(number, arr) {
  count = 0;

  for (let i = 0; i < number; i++) {
    if (arr[i] == number) {
      count = count + 1;
    }

    return count;
  }
}

arr = [1, 2, 3, 4, 1, 2];
let res = Chekc(arr);
console.log(res);
