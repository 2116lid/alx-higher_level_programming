#!/usr/bin/node

function recfact (n) {
  if (isNaN(n) || parseInt(n) === 1) {
    return 1;
  } else {
    return (parseInt(n) * recfact(parseInt(n) - 1));
  }
}
console.log(recfact(process.argv[2]));
