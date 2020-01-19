var express = require('express');
var app = express();

app.set('view engine', 'jade');
app.get('/', function(req, res){
    res.render('index', {
        'title': 'This is the freakin title',
        'message': 'Yay, you got the freakin message!!!'
    })
});

var port = 7000
var server = app.listen(port, function(){
    console.log('Server is listening on port: ' + port);
});