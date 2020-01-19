var mongoClient = require('mongodb').MongoClient;
var url = 'mongodb://localhost';
var connectOption = {
    useNewUrlParser: true,
    useUnifiedTopology: true
};

mongoClient.connect(url, connectOption,
    function(err, db){
        if(err) throw err;

        var dbo = db.db('EmployeeDB');
        // var temp = dbo.collection('Employee').find().toArray(function(err, res){
        //     if(err) throw err;

        //     console.log(res);
        // });

        var temp = dbo.collection('Employee').updateOne(
            {'Employee ID' : '1'},
            {$set: {
                "Employee Name" : "Don Juan"
            }}
        );

        var temp = dbo.collection('Employee').find().toArray(function(err, res){
            if(err) throw err;

            console.log(res);
        });
        
        db.close();
    });