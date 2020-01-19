var express = require('express');
var app = express();

app.route('/Node').get(function(req, res){
    res.send('Tutorial on Node');
});

app.route('/Angular').get(function(req, res){
   res.send('Tutorial on Angular'); 
});

app.route('/').get(function(req, res){
    res.send('This is the root tutorial page!');
});

app.listen(7000);