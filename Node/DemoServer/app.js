const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const mongoConnect = require("./utils/database").mongoConnect;

// const adminRoutes = require("./routes/admin");
// const shopRoutes = require("./routes/shop");
const Product = require('./models/product')



const app = express();

app.use(
  bodyParser.urlencoded({
    extended: true
  })
);

app.use(express.static(path.join(__dirname, "public")));

// //created routes
// app.use("/admin", adminRoutes);
// app.use(shopRoutes);




app.use((req, res, next) => {
  res.status(404).send("Page not found.");
});

function addProduct(){
  const product = new Product("newP", "99.99", "description", "none");
  product.save().then(res =>{
    console.log(res)
  }).catch(e => console.log(e));
}




mongoConnect(() => {
  app.listen(3000, () => {
    console.log("Server listening on port 3000");
    addProduct();
  });
});


