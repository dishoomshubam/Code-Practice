const expr = "Papayas";
switch (expr) {
  case "Oranges":
    console.log("Oranges are $0.59 a pound.");
    break;
  case "Mangoes":
  case "Papayas":
    console.log("Mangoes and papayas are $2.79 a pound.");
    // Expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log(`Sorry, we are out of ${expr}.`);
}

function result(a) {
  let output;
  switch (true) {
    case a > 80:
      output = "goof";
      break;
    case a > 65 && a <= 80:
      output = "okay";
      break;
    case a > 50 && a <= 65:
      output = "bad";
      break;
    default:
      output = "fail";
  }
  return output;
}

console.log(result(70)); // Output will be "okay"
