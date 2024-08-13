/*If, else, elseif

if constion are always print a truce condtion
else if statemnt are used a your code are complex you need to multiplibe condtion this time used a else if statment
else used a false stament a constion

*/

function x() {
  let y = 10;

  if (y < 11) {
    console.log("true");
  } else {
    console.log("false");
  }
}

x();

/*
Task 
You don't need to read input or print anything. Your task is to complete the function compareNM() which takes two integer n and m
as input parameters and returns string

'lesser' if n < m
'equal' if n == m
'greater' if n > m


*/

function compare(a, b) {
  let result;
  if (a < b) {
    result = "lesser";
  } else if (a > b) {
    result = "greter";
  } else {
    result = "equal";
  }

  return result;
}

console.log(compare(8, 8));

////////////////////////////////////////////////////

//  One more a example

function positiveNum(x) {
  let result;
  if ((x) => 10) {
    result = "positiveNum";
  } else {
    result = "Negative Number";
  }
  return result;
}

console.log(positiveNum(15));

// else if Condition

function multipleCheck(x) {
  let value;
  if (x == 10) {
    value = "same";
  } else if (x <= 10) {
    value = "less then 10";
  } else if (x > 10) {
    value = "more then 10";
  } else {
    value = "not in this";
  }

  return value;
}

console.log(multipleCheck(9));

function checkValue(a, b) {
  if (a === 1) {
    if (b === 2) {
      console.log("a is 1 and b is 2");
    }
  } else {
    console.log("a is not 1");
  }
}
checkValue();
