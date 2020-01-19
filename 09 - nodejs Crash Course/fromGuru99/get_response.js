var request = require('request')
request.get('https://www.google.com', function(error, response, body){
    // console.log(error);
    // console.log(response);
    console.log(body);
});