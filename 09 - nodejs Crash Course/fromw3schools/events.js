var events = require('events');
var eventEmitter = new events.EventEmitter()

var myEventHandler = function(){
    console.log('This is the coolest event!');
};

eventEmitter.on('hit', myEventHandler);
eventEmitter.emit('hit');
