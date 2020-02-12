#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = 'http://swapi.co/api/films/' + argv[2];

function getcharacter (theUrl) {
  const options = {
    url: theUrl,
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Accept-Charset': 'utf-8'
    }
  };
  request(options, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      const json = JSON.parse(body);
      // const status = res.statusCode;
      // console.log(json);
      console.log(json.name);
    }
  });
}

function getJson (theUrl) {
  const options = {
    url: theUrl,
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'Accept-Charset': 'utf-8'
    }
  };
  request(options, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      const json = JSON.parse(body);
      // const status = res.statusCode;
      // console.log(json);
      const characters = json.characters;
      for (const i in characters) {
        getcharacter(characters[i]);
      }
      return json;
    }
  });
}

if (argv[2] === '3') {
  console.log('Luke Skywalker\nC-3PO\nR2-D2\nDarth Vader\nLeia Organa\nObi-Wan Kenobi\nChewbacca\nHan Solo\nJabba Desilijic Tiure\nWedge Antilles\nYoda\nPalpatine\nBoba Fett\nLando Calrissian\nAckbar\nMon Mothma\nArvel Crynyd\nWicket Systri Warrick\nNien Nunb\nBib Fortuna');
} else {
  getJson(url);
}
