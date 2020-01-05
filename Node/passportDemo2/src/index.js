const express = require('express')
const bodyParser = require('body-parser')
const passport = require('passport');

app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true}))

app.get("/", (req, res) => {
    res.json("Hello world")
})

app.listen(3000, () => console.log("Server listening on port 3000"));