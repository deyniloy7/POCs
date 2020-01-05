const mongodb = require("mongodb");
const MongoClient = mongodb.MongoClient;
const uri =
  "mongodb+srv://root:root@cluster0-d0wrq.mongodb.net/shop?retryWrites=true&w=majority";
// const client = new MongoClient(uri, { useNewUrlParser: true });
// client.connect(err => {
//   const collection = client.db("test").collection("devices");
//   // perform actions on the collection object
//   client.close();
// });

let _db;

const mongoConnect = callback => {
  MongoClient.connect(uri)
    .then(client => {
      _db = client.db();
      callback();
    })
    .catch(e => {
      console.log(e);
      throw e;
    });
};

const getDb = () => {
  if (_db) {
    return _db;
  }
  throw "No db found";
};


exports.mongoConnect = mongoConnect;
exports.getDb = getDb;
