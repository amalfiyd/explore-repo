// function* Add(x){
//     yield x+1;
//     var y = yield(null);
//     y = 6
//     return x+y;
// }

// var gen = Add(5);
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());
// console.log(gen.next());

function Timedelay(ptime, callback) {
    setTimeout(function() {
        callback("Pausing for " + ptime);
    }, ptime);
}

function* Messages(){
    console.log(yield(Timedelay(1000, function(){})));
    console.log(yield(Timedelay(2000, function(){})));
    console.log(yield(Timedelay(4000, function(){})));
}

var gen = Messages();
gen.next();