#!/usr/bin/node
const reques = require('request');
const url = process.argv[2];

reques(url, (err, response, body) => {
  if (err) { console.log(err); } else {
    const films = JSON.parse(body).results;
    const WedgeFilms = films.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(WedgeFilms.length);
  }
});
