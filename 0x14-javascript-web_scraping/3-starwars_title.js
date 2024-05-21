#!/usr/bin/node
const request = require('request');
const ID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + ID;

request(url, (err, response, body) => {
  if (err) { console.log(err); } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
