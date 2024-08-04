const radius = [3, 4, 2, 3, 2, 3, 4];
// Function to calculate the area of a circle given the radius
const area = function (radius) {
  return Math.PI * radius * radius; // Fixed the area formula
};

// Callback function that calculates based on the logic provided
const calculate = function (radius, logic) {
  const output = [];
  for (let i = 0; i < radius.length; i++) {
    output.push(logic(radius[i]));
  }
  return output;
};

// Call the calculate function with the radius array and the area function
console.log(calculate(radius, area));
