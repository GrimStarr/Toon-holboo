const express = require("express");
const router = express.Router();
const { PythonShell } = require("python-shell");

let python = new PythonShell("go.py", { mode: "text" });

router.get("/:arg", (req, res) => {
  let arg = req.params.arg;
  console.log(arg);
  let options = {
    args: [arg],
  };

  PythonShell.run("go.py", options, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      console.log(result);
    }
  });
  const yaml = require("js-yaml");
  const fs = require("fs");

  // Get document, or throw exception on error
  try {
    const doc = yaml.load(fs.readFileSync("./web.grc", "utf8"));
    console.log(doc.blocks);
    res.send(home);
  } catch (e) {
    console.log(e);
  }
});

// router.get("/back", (req, res) => {
//   return console.log("back");
// });

// router.get("/right", (req, res) => {
//   return console.log("right");
// });

// router.get("/left", (req, res) => {
//   return console.log("left");
// });

// router.get("/stop", (req, res) => {
//   return console.log("stop");
// });

module.exports = router;
