const express = require("express");
const path = require("path");

const app = express();
const port = 3000;

const moveController = require("./moveController");

app.use(express.json());
app.use("/api", moveController);

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  res.render("start");
});
app.get("/lab3", (req, res) => {
  res.render("lab3");
});
app.listen(port, () => console.log(`listening on port ${port}!`));

process.on("unhandledRejection", (err, promise) => {
  console.log(`Алдаа гарлаа: ${err.message}`);
  server.close(() => {
    process.exit(1);
  });
});
