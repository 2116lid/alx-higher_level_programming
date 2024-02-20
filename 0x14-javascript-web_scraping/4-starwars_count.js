#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmIndex in films) {
      const chr = films[filmIndex].characters;
      for (const charIndex in chr) {
        if (chr[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
