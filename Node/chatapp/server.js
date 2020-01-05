var express = require("express");
var mongoose = require("mongoose");
var bodyParser = require("body-parser");

var app = express();

var http = require("http").Server(app);
var io = require("socket.io")(http);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

var connString = "mongodb://127.0.0.1:27017/mylearning";
app.use(express.static(__dirname));

var Chats = mongoose.model("Chats", {
  name: String,
  chat: String
});

app.post("/chats", async (req, res) => {
  try {
    var chat = new Chats(req.body);
    await chat.save();
    res.sendStatus(200);
  } catch (e) {
    res.sendStatus(500);
    console.error(e);
  }
});

app.get("/chats", (req, res) => {
  Chats.find({}, (error, chats) => {
    res.send(chats);
  });
});

io.on("connection", socket => {
    console.log("Socket connected");
    
  });

mongoose
  .connect(
    connString,
    {
      useNewUrlParser: true,
      useUnifiedTopology: true
    },
    err => {
      if (err) console.log("Database connection", err);
    }
  )
  .then(() => {
    http.listen(3000, () => {
        console.log("App listening on port 3000");
      });
  });
