#!/usr/bin/node
const argv = process.argv;
if (typeof argv[2] === 'string' && !isNaN(argv[2])) {
  console.log('My number: ' + parseInt(argv[2]));
} else if (typeof argv[2] !== 'number' || argv[2] === undefined) {
  console.log('Not a number')
} else if (typeof argv[2] === 'number') {
  console.log('My number: ' + Math.floor(argv[2]));
} else {
  console.log('My number: ' + argv[2]);
}
