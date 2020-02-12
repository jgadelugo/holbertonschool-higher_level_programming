#!/usr/bin/node

const request = require("request")
const argv = process.argv;
const url = argv[2]


function getStatus(theUrl)
{
    const options = {
        url: theUrl,
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8'
        }
    };
    request(options, function(err, res, body) {
        if (err) {
            console.log(err)
        } else {
            //let json = JSON.parse(body);
            let status = res.statusCode
            console.log("code: " + status);
            return status;
        }
    });
}

getStatus(url)