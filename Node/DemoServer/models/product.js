// const mongoConnect = require("../utils/database").mongoConnect;
const getDb = require("../utils/database").getDb;

class Product {
  constructor(title, price, description, imageUrl) {
    this.title = title;
    this.price = price;
    this.description = description;
    this.imageUrl = imageUrl;
  }

  save() { 
    const db = getDb();
    return db
      .collection("products")
      .insertOne(this)
      .then(res => {
        console.log(res);
      })
      .catch(e => {
        throw e;
      }); 
  }
}

module.exports = Product;
