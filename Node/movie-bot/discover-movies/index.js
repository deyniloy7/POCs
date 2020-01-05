const config = require("../config");
const { discoverMovie } = require("./movieApi");

function loadMovieRoute(app) {
  app.post("/discover-movies", function(req, res) {
    console.log(req.body.conversation);
    const kind = req.body.conversation.memory["recording"].value;
    const genreId = req.body.conversation.memory["genre"].id;
    const language = req.body.conversation.memory["language"];
    const nationality = req.body.conversation.memory["nationality"];

    const isoCode = language
      ? language.short.toLowerCase()
      : nationality.short.toLowerCase();

    return discoverMovie(kind, genreId, isoCode)
      .then(function(carouselle) {
        res.json({
          replies: carouselle,
          conversation: {}
        });
      })
      .catch(function(err) {
          console.log(err.response)
        // res.send("movieApi::discoverMovie error", err);
      });
  });
}

module.exports = loadMovieRoute;