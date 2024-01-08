#!/usr/bin/node
let count = 0;
const argv = process.argv;
argv.forEach((arg, index) => {
  if (index >= 2) {
    count++;
  }
});
if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log(argv[2]);
}
